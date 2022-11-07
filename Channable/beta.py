import csv
from collections import OrderedDict as OrderedDict
def from_csv(fname):
    with open(fname, 'r') as data:
        drow = csv.DictReader(data)
        data = [r for r in drow]
    return data

def update_fields(dict_a, dict_b):
    changes = []
    for i, j in zip(dict_a.items(), dict_b.items()):
        if i != j:
            # print(j)
            changes.append(j)
    return changes


path_to_before_csv = "Channable/product_inventory_before.csv"
path_to_after_csv = "Channable/product_inventory_after.csv"

before = from_csv(path_to_before_csv)
after = from_csv(path_to_after_csv)
id = 'id'
results = []
for rowy in before:
    id_before = rowy[id]
    rowt = [row for row in after if row[id] == id_before]
    if not len(rowt):
        pass
        # item doesn't exist in new file, hence product will be deleted to keep product catalog updated
        results.append(OrderedDict({
            'operation_type': 'DELETE',
            'product_id': id_before,
            'product_data': str(dict(rowy))
        }))
    else:
        # item exists, will check if values are same if not, update with changes.
        ch = update_fields(rowy, rowt[0])
        if ch:
            results.append(OrderedDict({
                'operation_type': 'UPDATE',
                'product_id': id_before,
                'product_data': ch
            }))
        else:
            pass
for rowa in after:
    if not rowa['id'] in [rowb['id'] for rowb in before]:
        results.append(OrderedDict({
            'operation_type': 'CREATE',
            'product_id': rowa['id'],
            'product_data': str(dict(rowa))
        }))
