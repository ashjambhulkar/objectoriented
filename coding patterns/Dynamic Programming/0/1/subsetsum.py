# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

# Example 1:
# Input: {1, 2, 3, 7}, S = 6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}
# Example 2:
# Input: {1, 2, 7, 1, 5}, S = 10
# Output: True
# The given set has a subset whose sum is '10': {1, 2, 7}
# Example 3:
# Input: {1, 3, 4, 8}, S = 6
# Output: False
# The given set does not have any subset whose sum is equal to '6'.


def helper(arr, s):
  if len(arr) < 2:
    return False
  
  dp = [[False for _ in range(s+1)] for _ in range(len(arr))]

  for i in range(len(arr)):
    dp[i][0] = True

  dp[0][arr[0]] = True

  for i in range(1,len(arr)):
    for j in range(1, s+1):
      if arr[i] <= j:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
      else:
        dp[i][j] = dp[i-1][j]

  return dp[-1][-1]


arr = [1, 2, 3, 7]
print(helper(arr,6))
