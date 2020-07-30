# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

# Example 1:
# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
# Example 2:
# Input: {1, 2, 7, 1, 5}
# Output: 0
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
# Example 3:
# Input: {1, 3, 100, 4}
# Output: 92
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

def helper(arr):
  total = sum(arr)
  dp = [[False for _ in range(total//2+1)] for _ in range(len(arr))]

  for i in range(len(arr)):
    dp[i][0] = True
  
  dp[0][arr[0]] = True

  for i in range(1, len(arr)):
    for j in range(1, total//2+1):
      if j >= arr[i]:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
      else:
        dp[i][j] = dp[i-1][j]
  
  left = 0 
  for i in range(total//2, -1, -1):
    if dp[-1][i]:
      left = i
      break
  right = total - left
  return abs(left - right)


arr = [1, 2, 3, 4, 5]
print(helper(arr))
