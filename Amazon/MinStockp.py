stockPrice = [1, 3, 2, 3]
# returns 2
def findEarliestMonth(stockPrice):
    totalStockPrice = sum(stockPrice)
    minNetPrice = float('inf')
    earliestMonth = -1
    n = len(stockPrice)

    # Start with 0
    leftSum = 0
    # Start with totalSum
    rightSum = totalStockPrice

    for i in range(1, n):
        # Average of first i months - Average of rest of the months
        # Sum of First i months
        leftSum+=stockPrice[i-1]
        # Sum of rest of the months
        rightSum-=stockPrice[i-1]
        # Net Price from the definition
        netPrice = abs((leftSum//i - rightSum//(n-i)))

        # Update the netprice
        if minNetPrice > netPrice:
            minNetPrice = netPrice
            earliestMonth = i
    return earliestMonth