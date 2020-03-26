# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# Input: Fruit = ['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray['C', 'A', 'C']


def helper(arr):
  if not arr:
    return 0
  start = 0
  count = 0
  hashmap = {}
  for end in range(len(arr)):
    end_char = arr[end]
    if end_char not in hashmap:
      hashmap[end_char] = 0
    hashmap[end_char] += 1
  while len(hashmap) > 2:
    start_char = arr[start]
    hashmap[start_char] -= 1
    if hashmap[start_char] == 0:
      del hashmap[start_char]
    start += 1
  count = max(count, end-start+1)
  return count


# arr = ['A', 'B', 'C', 'A', 'C']
arr = ['A', 'B', 'C', 'B', 'B', 'C']
print(helper(arr))
