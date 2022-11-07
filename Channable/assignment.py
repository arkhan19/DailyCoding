"""
Hello Python developer

Good luck with this coding exercise for becoming a Python developer at Channable!

# First, some context:
Channable is an online tool that imports products from its users' eCommerceplatforms (e.g. WooCommerce) every day, 
processes those products, and sends updates for those products to marketing channels (e.g. Amazon or eBay). 
Technically speaking, Channable sends ​create​, ​update, and ​delete​ operations for these products. Every day when 
Channable imports the products from the eCommerce platform, Channable needs to decide which operation it needs 
to send to the marketing channel:

  - Create: ​the product wasn’t imported from the eCommerce system yesterday, 
    but it was imported today. This means we have to send a ​create operation 
    ​to the eCommerce platform

  - Update:​ the product was imported yesterday and is also imported today, 
    however, one of the values for the products has changed (e.g. the price of
    the product). This means we have to send an ​update operation​ to the 
    marketing channel

  - Delete: ​the product was imported yesterday, but was not imported today. 
    This means we have to send a ​delete operation ​to the marketing channel


# The assignment:
In this assignment you are asked to make a basic implementation of the logic described above. You should have
received two CSV files to resemble the data that is imported from the eCommerce system:

  - product_inventory_before.csv​ (resembles the product data that was imported yesterday)
  - product_inventory_after.csv ​(resembles the product data that was imported today)

For this assignment you need to build a program that compares the product data between the `before CSV` and 
the `after CSV`. The `​id​` column can be assumed to be a unique identifier for the products in both CSVs. The 
output should give the create, update, and delete operations that should be sent to the marketing channel.


# Requirements:
  - The program should be a single ​.py ​​file (no compressed files, such as .zip, .rar, etc.)
  - The program should be written in ​python 3.7​, using only python’s ​built-in libraries.
  - You have to implement the `ProductDiffer` class below and specifically its entry point called `main`. 
  - The `ProductStreamProcessor` should not be changed.
  - The output of main is a sequence of operations in the form of triples that contain:
        1. the operation type
        2. the product id
        3. either a dictionary with the complete product data where the keys are the column names
           from the CSV files or a `None`


# Note:
The assignment is consciously kept a bit basic to make sure you don’t have to spend hours and hours on this 
assignment. However, even though the assignment itself is quite basic, we would like you to show us how you 
would structure your code to make it easily readable, so others can trust it works as intended.
"""
import abc
from enum import Enum, auto
from typing import Tuple, Optional, Dict, Iterator, Any

import csv
from collections import OrderedDict as OrderedDict


class Operation(Enum):
    CREATE = auto()
    UPDATE = auto()
    DELETE = auto()


class ProductStreamProcessor(metaclass=abc.ABCMeta):
    # Note the methods of this ProductStreamProcessor class should not be adjusted
    # as this is a hypothetical base class shared with other programs. 

    def __init__(self, path_to_before_csv: str, path_to_after_csv: str):
        self.path_to_before_csv = path_to_before_csv
        self.path_to_after_csv = path_to_after_csv

    @abc.abstractmethod
    def main(self) -> Iterator[Tuple[Operation, str, Optional[Dict[str, Any]]]]:
        """
        Creates a stream of operations based for products in the form of tuples
        where the first element is the operation, the second element is the id
        for the product, and the third is a dictionary with all data for a 
        product. The latter is None for DELETE operations.
        """
        ...


class ProductDiffer(ProductStreamProcessor):
    """
    Implement this class to create a simple product differ.
    """

    def from_csv(self, fname):
        with open(fname, 'r') as data:
            drow = csv.DictReader(data)
            data = [r for r in drow]
        return data

    def update_fields(self, dict_a, dict_b):
        changes = []
        for i, j in zip(dict_a.items(), dict_b.items()):
            if i != j:
                changes.append(j)
        return changes

    def main(self):
        """
        Case 1: Delete if found in before but no in after
        Case 2: Update with recorded changes, if found in both, but with changes in after.
        Case 3: Create if found in after but not in before.
        :return:
        list res containing Dicts with 'operation_type', 'product_id', and 'product_data'
        """
        before = self.from_csv(self.path_to_before_csv)
        after = self.from_csv(self.path_to_after_csv)
        id = 'id'
        results = []
        for rowb in before:
            id_before = rowb[id]
            rowa = [row for row in after if row[id] == id_before]
            if not len(rowa):
                # rowb[id] doesn't exist in new file, hence product will be deleted
                results.append( OrderedDict({
                    'operation_type': 'DELETE',
                    'product_id': id_before,
                    'product_data': None
                }))
            else:
                # item exists, will check if values are same if not, update with changes.
                ch = self.update_fields(rowb, rowa[0])
                # changes are recorded, if not
                if ch:
                    ret = OrderedDict({
                        'operation_type': 'UPDATE',
                        'product_id': id_before,
                        'product_data': ch
                    })
                    results.append(ret)
                else:
                    pass
        for rowa in after:
            # iteam in after, but not in before, so will create the new item.
            if not rowa['id'] in [rowb['id'] for rowb in before]:
                results.append(OrderedDict({
                    'operation_type': 'CREATE',
                    'product_id': rowa['id'],
                    'product_data': str(dict(rowa))
                }))
        # Sort Results
        results = sorted(results, key=lambda x: x['product_id'])
        return results
