# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

def helper(arr, k):
  maximum = 0
  temp = 0
  start = 0
  for end in range(len(arr)):
    temp += arr[end]
    if end >= k-1:
      maximum = max(maximum, temp)
      temp -= arr[start]
      start += 1
  return maximum
  
  
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(helper(arr, k))
