# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
# Input: [2, 5, 3, 10], target = 30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.

from collections import deque


def helper(arr, target):
  result = []
  start = 0
  product = 1
  for end in range(len(arr)):
    product *= arr[end]
    while product >= target and start < len(arr):
      product //= arr[start]
      start += 1
    temp = deque()
    # temp = []
    for i in range(end, start-1, -1):
      # temp.append(arr[i])
      temp.appendleft(arr[i])
      result.append(list(temp))
      # result.append(list(temp))
  return result


arr = [2, 5, 3, 10]
target = 30
print(helper(arr, target))
