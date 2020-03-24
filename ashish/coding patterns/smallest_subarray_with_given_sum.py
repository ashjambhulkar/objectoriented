def helper(arr, k):
  start = 0 
  end = 0
  temp = 0
  result = float("-inf")
  for end in range(len(arr)):
    temp += arr[start]
    while temp >= k:
      result = min(result, end-start+1)
      temp -= arr[start]
      start += 1
  if result == float("-inf"):
    return 0
  return result