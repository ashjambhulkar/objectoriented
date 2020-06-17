# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]


def helper(arr):
  low = 0
  high = len(arr)-1
  i = 0
  while i <= high:
    if arr[i] == 0:
      arr[i], arr[low] = arr[low], arr[i]
      i += 1
      low += 1
    elif arr[i] == 1:
      i += 1
    else:
      arr[i], arr[high] = arr[high], arr[i]
      high -= 1


arr = [1, 0, 2, 1, 0]
print(helper(arr))
