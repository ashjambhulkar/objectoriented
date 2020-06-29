# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# Input: Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k = 2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

import collections


def helper(string, k):
  hashmap = {0: 0, 1: 0}
  count = 0
  result = 0
  start = 0
  for end in range(len(string)):
    end_char = string[end]
    hashmap[end_char] += 1
    if hashmap[0] == k:
      result = max(result, end-start+1)
    while hashmap[0] > k:
      start_char = string[start]
      if start_char == 0:
        hashmap[0] -= 1
      start += 1
  return result



arr = [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1]
k = 2
print(helper(arr, k))

