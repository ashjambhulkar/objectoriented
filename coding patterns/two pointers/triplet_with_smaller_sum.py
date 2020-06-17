# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
# Input: [-1, 0, 2, 3], target = 3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


def helper(arr, target):
  arr.sort()
  count = 0
  for i in range(len(arr)-2):
    count += search_triplet(arr, target-arr[i], i+1)
  return count


def search_triplet(arr, test, start):
  count = 0
  end = len(arr) - 1
  while start < end:
    if arr[start] + arr[end] < test:
      count += end - start
      start += 1
    else:
      end -= 1
  return count

arr = [-1, 0, 2, 3]
target = 3
# arr = [-1, 4, 2, 1, 3]
# target = 5  
print(helper(arr, target))
