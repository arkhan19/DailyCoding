N = 10
K = 1
M = 2
S = [2, 6]

N = 15
K = 2
M = 3
S = [11, 6, 14]

# nod = [-1 if x+1 in S else 0 for x in range(N)]
nod = {x:-1 if x+1 in S else 0 for x in range(N)}
# nod = {x:-1 if x+1 in S else 0 for x in range(N)}
indices = [index for index, _val in enumerate(nod)]
# do_X() if len(your_list) > your_index else do_something_else()
# for k, v in enumerate(nod):
#     if k+1 in S:
#         if k - K in indices:
#             nod[k - K] = -1
#         if k + K in indices:
#             nod[k + K] = -1



# count = 0
for k, v in enumerate(nod):
    if v == 0:
        print(f'INDEX{k}')
        if nod[k::-1][1:K + 1] and -1 not in nod[k::-1][1:K + 1]:
            print(f'BEHIND{nod[k::-1][1:K + 1]}')
            if nod[k::][1:K + 1] and -1 not in nod[k::][1:K + 1]:
                print(f'AHEAD{nod[k::][1:K + 1]}')


# for k, v in enumerate(nod):
#     if v == 0:
#         # left of a number : h[i::-1][1:K+1]
#         # right of a number : h[i::][1:K+1]
#         if -1 in nod[k::-1][1:K+1] and -1 in nod[k::][1:K+1]:
#             nod[k::][1:K + 1] = -1
#             print(f'INDEX{k}')
#
#         print(f'BEHIND{nod[k::-1][1:K+1]}')
#         print(f'AHEAD{nod[k::][1:K+1]}')









# for k, v in enumerate(nod):
#     if v == 0:
#         if k == 0 or k == N-1:
#             if k==0:
#                 print(f"FINDEX = {k+K}")
#                 if nod[k+K] != -1:
#                     nod[k] = 2
#                     nod[k+K] = -1
#                     break
#             if k==N-1:
#                 print(f"LINDEX = {k-K}")
#                 if nod[k - K] != -1:
#                     nod[k] = 2
#                     nod[k - K] = -1
#                     break
#         if 0<k<N-1:
#             if k+K<N-1:
#                 print(f"CINDEX = {k+K}")
#                 if nod[k + K] != -1:
#                     nod[k] = 2
#                     nod[k + K] = -1
#             if k-K>0:
#                 print(f"CINDEX = {k-K}")
#                 if nod[k - K] != -1:
#                     nod[k] = 2
#                     nod[k - K] = -1


# from collections import OrderedDict
# od = OrderedDict()
# for x in range(N):
#     if x+1 in S:
#         od[x] = -1
#     else:
#         od[x] = 0

# sum(1 for val in nod if val==0)
print(count)
# count = sum(x == 0 for x in nod.values())


# count = sum(x == 0 for x in nod.values())



# filtered = list(filter(lambda num: num > N, list(nod.keys())))
# [nod.pop(key) for key in filtered]

# nod = []

# for i in range (1, N+1):
#     if i in S:
#         nod.append(-1)
#     else:
#         nod.append(0)
#
# for k, v in enumerate(nod):
#     if v == -1:
#         for x in range(1, K+1):
#             if k-x >= 0:
#                 print(f"B = {k - x}")
#                 nod[k-x] = -1
#             if k+x+1 <= N-1:
#                 print(f"A = {k + x + 1}")
#                 nod[k+x+1] = -1
#
# for k, v in enumerate(nod):
#     if k+1 in S:
#         for x in range(1, K + 1):
#             if k - x >= 0:
#                 nod[k - x] = -1
#             if k + x < N:
#                 nod[k + x] = -1
# count = sum(1 for val in nod if val==0)


# for k, v in enumerate(nod):
#     if (k + 1) in S:
#         for x in range(0, K + 1):
#             if k - x >= 0:
#                 nod[k - x] = -1
#             if k + x < N:
#                 nod[k + x] = -1