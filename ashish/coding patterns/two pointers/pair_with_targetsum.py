# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Input: [1, 2, 3, 4, 6], target = 6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4 = 6

# def helper(arr, target_sum):
#   start = 0
#   end = len(arr)-1
#   while start < end:
#     total = arr[start] + arr[end]
#     if total == target_sum:
#       return [start, end]
#     if total > target_sum:
#       end -= 1
#     if total < target_sum:
#       start += 1
#   return [-1, -1]

# by using hashtable 
def helper(arr, target):
  hashmap = {}
  for i, val in enumerate(arr):
    if target - val in hashmap:
      return [hashmap[target-val], i]
    hashmap[val] = i
  return [-1, -1]


arr = [1,2,3,4,6]
target = 6
print(helper(arr, target))
