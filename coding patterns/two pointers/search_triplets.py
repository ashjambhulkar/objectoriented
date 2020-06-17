# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

def helper(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    sort_the_triplet(arr, -arr[i], i+1, triplets)
 
def sort_the_triplet(arr, target, start, triplets):
  end = len(arr) - 1
  while start < end:
    total = arr[start] + arr[end]
    if total == target:
      triplets.append([-target, arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start-1]:
        start += 1
      while start < end and arr[end] == arr[end+1]:
        end -= 1
    elif total > target:
      end -= 1
    else:
      start += 1


arr = [-3, 0, 1, 2, -1, 1, -2]
print(helper(arr))

