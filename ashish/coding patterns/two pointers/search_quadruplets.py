# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
# Input: [4, 1, 2, -1, 1, -3], target = 1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.


def helper(arr, target):
  arr.sort()
  quadruplets = []
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      # if j > 0 and arr[j] == arr[j-1]:
      #   continue
      search_pairs(arr, arr[i], arr[j], j+1, quadruplets, target)
  return quadruplets


def search_pairs(arr, first, second, start, quadruplets, target):
  end = len(arr) - 1
  while start < end:
    temp = first + second + arr[start] + arr[end]
    if temp == target:
      quadruplets.append([first, second, arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start-1]:
        start += 1
      while start < end and arr[end] == arr[end+1]:
        end -= 1
    elif temp < target:
      start += 1
    else:
      end -= 1
  


arr = [4, 1, 2, -1, 1, -3]
target = 1
print(helper(arr, target))
