# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# Input: Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k = 2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

def helper(arr, k):
  start = 0
  count = 0
  result = {}
  length = 0
  for end in range(len(arr)):
    end_num = arr[end]
    if end_num not in result:
      result[end_num] = 0
    result[end_num] += 1
    count = max(count, result[end_num])
    if end-start+1 - count > k:
      start_num = arr[start]
      result[start_num] -= 1
      start += 1
    length = max(length, end-start+1)
  return length


arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
print(helper(arr, k))

