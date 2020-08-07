# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

# Example 1:
# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
# Example 2:
# Input: {1, 1, 3, 4, 7}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
# Example 3:
# Input: {2, 3, 4, 6}
# Output: False
# Explanation: The given set cannot be partitioned into two subsets with equal sum.



def subset(arr):
  if len(arr) < 2:
    return False
  s = sum(arr)
  if s % 2 != 0:
    return False

  dp = [[False for _ in range(s//2+1)] for _ in range(len(arr))]

  for i in range(len(arr)):
    dp[i][0] = True

  dp[0][arr[0]] = True 

  for i in range(1, len(arr)):
    for j in range(1, s//2+1):
      if arr[i] <= j:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]] 
      else:
        dp[i][j] = dp[i-1][j]
  return dp[-1][-1]


print(subset([1, 1, 3, 4, 7]))
