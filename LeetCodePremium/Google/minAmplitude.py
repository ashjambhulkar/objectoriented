# Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of the array(basically difference between largest and smallest element).

# Example 1:

# Input: [-1, 3, -1, 8, 5 4]
# Output: 2
# Explanation: we can change - 1, -1, 8 to 3, 4 or 5
# Example 2:

# Input: [10, 10, 3, 4, 10]
# Output: 0
# Explanation: change 3 and 4 to 10


def helper(arr):
  arr.sort()
  ans = arr[-1] - arr[0]
  left = 0
  right = len(arr)-4
  while right < len(arr):
    ans = min(ans, arr[right]-arr[left])
    right += 1
    left += 1
  print(ans)


arr = [-1, 3, -1, 8, 5, 4, 9,11]
helper(arr)
