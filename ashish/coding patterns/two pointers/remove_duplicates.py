# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space
# after removing the duplicates in-place return the new length of the array.
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be[2, 3, 6, 9].


def helper(arr):
  start = len(arr)-2
  end = len(arr) - 1
  while end is not 0:
    if arr[start] == arr[end]:
      del arr[end]
      end = start
      start -= 1
    else:
      start -= 1
      end -= 1
  return arr


arr = [2, 3, 3, 3, 6, 9, 9]
# arr = [2,2]
print(helper(arr))