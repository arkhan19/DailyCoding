import argparse
from collections import OrderedDict as ODict
import csv
from io import StringIO
import json

from dictdiffer import diff # https://pypi.org/project/dictdiffer


def from_csv(fname):
  with open(fname, 'r') as inf:
    dialect = csv.Sniffer().sniff(inf.readline(), delimiters=['\t',','])
    inf.seek(0)
    dr = csv.DictReader(inf, dialect=dialect)
    dat = [d for d in dr]
  return dat


def main(ID, fnames):
  dat0, dat1 = [from_csv(fn) for fn in fnames]

  if not len(ID): ID = list(dat0[0].keys())[0] # get *1st* key/column

  res = []
  for d0 in dat0:
    id = d0[ID]
    d1 = [d for d in dat1 if d[ID]==id] # find id in dat1...
    if not len(d1): # if not found
      res.append(ODict({
        ID: id,
        'Diff': 'REMOVED', ## 'REMOVED'
        'Details': str(dict(d0)) #json.dumps(d0)
      }))
    else:
      d1 = d1[0]
      diffs = list( diff(d0, d1) ) # find changes...
      if not diffs: pass # if none
      else:
        res.append(ODict({
          ID: id,
          'Diff': 'CHANGED', ## 'CHANGED'
          'Details': '; '.join(F"{col}: {v[0]} => {v[1]}" for _,col,v in diffs)
        }))

  res += [
    ODict({
      ID: d1[ID],
      'Diff': 'ADDED', ## 'ADDED'
      'Details': str(dict(d1)) #json.dumps(d1)
    }) ## 'Added'
    for d1 in dat1
    if not d1[ID] in [d0[ID] for d0 in dat0]
  ]
  res = sorted(res, key=lambda x: x[ID]) # SORT

  s = ''
  sio = StringIO(s)
  with sio as outf:
    dw = csv.DictWriter(outf, fieldnames=res[0].keys(), quotechar='"')
    dw.writeheader()
    dw.writerows(res)
    s = sio.getvalue()
  print(s)


if __name__ == '__main__':
  argp = argparse.ArgumentParser(description='Find DIFFerences between two CSV files.')
  argp.add_argument('-k','--key', default='',
    help='Name of UNIQUE Key/Column [Default: *1st* key/column]')
  argp.add_argument('filename_0', help='Name of *first* FILE')
  argp.add_argument('filename_1', help='Name of *second* FILE')

  args = argp.parse_args() #vars(argp.parse_args())
  main(ID=args.key, fnames=[args.filename_0, args.filename_1])
