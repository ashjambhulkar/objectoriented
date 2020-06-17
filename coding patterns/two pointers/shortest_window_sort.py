# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray[5, 3, 7, 10, 9] to make the whole array sorted


def helper(arr):
  low = 0
  high = len(arr)-1
  while low < len(arr)-1 and arr[low] <= arr[low+1]:
    low += 1
  
  if low == len(arr)-1:
    return 0
  
  while high > 0 and arr[high] >= arr[high-1]:
    high -= 1
  
  subarray_min = min(arr[low:high+1])
  subarray_max = max(arr[low:high+1])

  while low > 0 and arr[low-1] >= subarray_min:
    low -= 1
  while high < len(arr)-1 and subarray_max >= arr[high+1]:
    high += 1

  return high - low + 1


arr = [1, 3, 2, 0, -1, 7, 10]
print(helper(arr))
