N = 10
K = 1
M = 2
S = [2, 6]

N = 15
K = 2
M = 3
S = [11, 6, 14]

nod = [-1 if x+1 in S else 0 for x in range(N)]
indices = [index for index, _val in enumerate(nod)]
for k, v in enumerate(nod):
    if k+1 in S:
        if k - K in indices:
            nod[k - K] = -1
        if k + K in indices:
            nod[k + K] = -1

for k, v in enumerate(nod):
    if v == 0:
        if k - K in indices:
            nod[k - K] = -1
        if k + K in indices:
            nod[k + K] = -1
