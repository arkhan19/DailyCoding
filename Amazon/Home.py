# Recursive Python3 program for
# coin change problem.

# Returns the count of ways we can sum
# coins[0...n-1] coins to get sum "sum"
def count(coins, sum):
  # We need sum+1 rows as the table is constructed
  # in bottom up manner using the base case 0 value
  # case (sum = 0)
  n = len(coins)
  table = [[0 for x in range(n)] for x in range(sum + 1)]

  # Fill the entries for 0 value case (n = 0)
  for i in range(n):
    table[0][i] = 1

  # Fill rest of the table entries in bottom up manner
  for i in range(1, sum + 1): # columns
    for j in range(n): # rows
      # Count of solutions including coins[j]
      # copy above value
      x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0

      # Count of solutions excluding coins[j]
      y = table[i][j - 1] if j >= 1 else 0

      # total count = excluding + including
      table[i][j] = x + y

  return table[sum][n - 1] # last cell


# Driver program to test above function
coins = [8,3, 1, 2]
n = len(coins)
print(count(coins, 0))