import collections
import typing
import unittest
from typing import List, Dict


def is_valid_cin(cin: str) -> bool:
    if isinstance(cin, str):
        arr = [int(i) for i in cin]  # Convert cin to array
        checksum = 0  # initiate checksum to zero
        for i in range(0, len(arr) - 2):
            checksum += ((i + 1) * arr[i])  # multiply with position
        if checksum % 97 == int(cin[12:14]):
            return True
        else:
            return False
    else:
        raise ValueError("CIN needs to be a string")


def calculate_inventory(start_inventory, transaction_log: str) -> Dict[str, int]:
    # if not isinstance(start_inventory, collections.abc.Mapping):
    #     raise ValueError("start_inventory should be a dictionary")
    # if not isinstance(transaction_log, str):
    #     raise ValueError("transaction_log should be in string format")

    entries = {}  # Empty Dict for transaction records
    for lines in transaction_log.splitlines():
        line = lines.split(' ')
        if line[0] in entries.keys():  # Update an entry
            if line[1] == 'INCOMING':
                entries[line[0]].append('+' + line[2])
            else:
                entries[line[0]].append('-' + line[2])
        else:  # Add new entry
            if line[1] == 'INCOMING':
                entries[line[0]] = ['+' + line[2]]
            else:
                entries[line[0]] = ['-' + line[2]]

    # Entries after reading the entire transaction log
    for k, v in entries.items():
        temp = list(int(item) for item in v)  # create a list of all outcoming to sum it
        entries[k] = sum(temp)

    # A copy of start of the day inventory
    new_inventory = start_inventory.copy()
    for k, v in entries.items():
        try:
            new_inventory[k] = new_inventory[k] + v  # Add the start of the day stock to the log values
        except KeyError:
            pass

    for k, v in new_inventory.items():
        if v < 0:  # Check if inventory is below zero
            # print("Stock for CIN{} below 0.".format(k))
            # new_inventory[k] = 0
            raise ValueError("Stock for CIN{} below 0".format(k))
    return new_inventory


class BestSeller:
    def __init__(self, cin, quantity_sold, pubtype=None):
        self.cin = cin
        self.quantity_sold = quantity_sold
        self.publication_type = pubtype

    @property
    def info(self):
        return "CIN:{} - Sold:{}".format(self.cin, self.quantity_sold)


def pub_type(cin):
    pub_type = cin[:2]
    if pub_type == '17':
        return 'Book'
    if pub_type == '42':
        return 'Magazine'


def calculate_best_sellers(transaction_log: str, n: int, publication_type: typing.Optional[str], ) \
        -> List[BestSeller]:
    # transaction_log = """17000372214424 INCOMING 9
    # 17000372214424 OUTGOING 1
    # 17000372214424 INCOMING 3
    # 42100551007977 OUTGOING 3
    # 42100551007977 INCOMING 1
    # 17000372214424 OUTGOING 4
    # 17000372214423 INCOMING 1
    # 17000372214423 OUTGOING 10
    # 42100551007971 OUTGOING 11
    # 42100551007971 INCOMING 5"""

    entries = {}  # Empty Dict for transaction records
    # record number of sold copies for each CIN which are outgoings
    for lines in transaction_log.splitlines():
        line = lines.split(' ')
        if line[0] in entries.keys():  # Update an entry
            if line[1] == 'OUTGOING':
                entries[line[0]].append('+' + line[2])
        else:  # Add new entry
            if line[1] == 'OUTGOING':
                entries[line[0]] = ['+' + line[2]]

    # Entries after reading the entire transaction log
    for k, v in entries.items():
        temp = list(int(item) for item in v)  # create a list of all incoming and outcoming to sum it
        entries[k] = sum(temp)

    books = {k: entries[k] for k in sorted(entries, key=entries.get, reverse=True)}
    best_sellers = []

    for key, value in books.items():
        if value is not 0:
            # Additional requirements 1
            if publication_type is None:
                best_sellers.append(BestSeller(cin=key, quantity_sold=value))
            else:
                best_sellers.append(BestSeller(cin=key, quantity_sold=value, pubtype=pub_type(cin=key)))

    if n >= len(best_sellers):
        # Additional requirements 0
        n = len(best_sellers)

    return best_sellers[:n]


class TestInventory(unittest.TestCase):
    def test_is_valid_cin_n(self):
        # Checks if incorrect cin is handled
        self.assertTrue(is_valid_cin(cin="17000372214424"))

    def test_is_valid_cin_p(self):
        # Checks if correct cin is processed
        self.assertFalse(is_valid_cin(cin="17000372214423"))

    def test_calculate_inventory_p(self):
        # Checks if correct inventory is produced
        test_new_inventory = {"17000372214424": 17, "42100551007977": 17}
        # test_news_inventory = {"17000372214424": 18, "42100551007977": 17}
        start_inventory = {"17000372214424": 10, "42100551007977": 19}
        transaction_log = """17000372214424 INCOMING 9 \n17000372214424 OUTGOING 1 \n17000372214424 INCOMING 3 \n42100551007977 OUTGOING 3 \n42100551007977 INCOMING 1 \n17000372214424 OUTGOING 4 """
        self.assertDictEqual(test_new_inventory, calculate_inventory(start_inventory, transaction_log))

    def test_calculate_best_sellers(self):
        # Checks the returned list has instances from best seller class
        transaction_log = """17000372214424 INCOMING 9 \n17000372214424 OUTGOING 1 \n17000372214424 INCOMING 3 \n42100551007977 OUTGOING 3 \n42100551007977 INCOMING 1 \n17000372214424 OUTGOING 4 """
        n = 2
        publication_type = "Magazine"
        best_sellers = calculate_best_sellers(transaction_log, n, publication_type)
        self.assertIsInstance(best_sellers[0], BestSeller)

    def test_calculate_best_sellers_c(self):
        # checks if correct number of books are returned
        transaction_log = """17000372214424 INCOMING 9 \n17000372214424 OUTGOING 1 \n17000372214424 INCOMING 3 \n42100551007977 OUTGOING 3 \n42100551007977 INCOMING 1 \n17000372214424 OUTGOING 4 """
        n = 2
        publication_type = "Magazine"
        best_sellers = calculate_best_sellers(transaction_log, n, publication_type)
        self.assertAlmostEqual(n, len(best_sellers))
