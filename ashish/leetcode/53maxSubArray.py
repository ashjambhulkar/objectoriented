# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

def helper(arr):
  curr = total = arr[0]
  for i in range(1, len(arr)):
    curr = max(arr[i], curr+arr[i])
    total = max(curr, total)
  return total


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(helper(arr))
