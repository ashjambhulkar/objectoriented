#Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

def helper(arr, k):
  if not arr:
    return 0
  start = 0
  result = []
  temp = 0
  for end in range(len(arr)):
    temp += arr[end]
    if end >=k-1:
      result.append(temp/k)
      temp -= arr[start]
      start += 1
  return result

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(helper(arr, k))
  
