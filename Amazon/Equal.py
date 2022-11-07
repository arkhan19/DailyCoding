def equal(arr):
    min = min(arr)

    for i in range(0, 5):
        ops = 0
        for j in range(len(arr)):
            t = arr[j] - (min - i)
            ops += t/5 + t%5/2 + t%5%2
        ans = min(ops)

    return ans