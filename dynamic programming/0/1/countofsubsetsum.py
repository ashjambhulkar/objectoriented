# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# Example 1:
# Input: {1, 1, 2, 3}, S = 4
# Output: 3
# The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
# Note that we have two similar sets {1, 3}, because we have two '1' in our input.
# Example 2:
# Input: {1, 2, 7, 1, 5}, S = 9
# Output: 3
# The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}


def helper(arr, result, target):
  count = 0
  def backtracking(arr, result):
    nonlocal count
    if sum(result) == target:
      print(result)
      count += 1
      return
    for i in range(len(arr)):
      result.append(arr[i])
      backtracking(arr[i+1:], result)
      result.pop()
  backtracking(arr, result)
  return count


arr = [1, 2, 7, 1, 5]
print(helper(arr, [],9))
  
