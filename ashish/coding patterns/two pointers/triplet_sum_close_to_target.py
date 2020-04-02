# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# Input: [-2, 0, 1, 2], target = 2
# Output: 1
# Explanation: The triplet[-2, 1, 2] has the closest sum to the target.


def helper(arr, k):
  arr.sort()
  small_diff = float("inf")
  for i in range(len(arr)-2):
    left  = i + 1
    right = len(arr) - 1
    while left < right:
      target_diff =  k - arr[i] - arr[left] - arr[right]
      if target_diff == 0:
        return k
      if abs(target_diff) < abs(small_diff) or (abs(target_diff) == abs(small_diff) and target_diff > small_diff):
        small_diff = target_diff
      if target_diff > 0:
        left += 1
      else:
        right -= 1
      small_diff = min(small_diff, target_diff)
  return abs(small_diff)


arr = [-3, -1, 1, 2]
k = 1
print(helper(arr, k))



      

# def triplet_sum_close_to_target(arr, target_sum):
#   arr.sort()
#   smallest_difference = math.inf
#   for i in range(len(arr)-2):
#     left = i + 1
#     right = len(arr) - 1
#     while (left < right):
#       target_diff = target_sum - arr[i] - arr[left] - arr[right]
#       if target_diff == 0:  # we've found a triplet with an exact sum
#         return target_sum - target_diff  # return sum of all the numbers

#       # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
#       if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
#         smallest_difference = target_diff  # save the closest and the biggest difference

#       if target_diff > 0:
#         left += 1  # we need a triplet with a bigger sum
#       else:
#         right -= 1  # we need a triplet with a smaller sum

#   return target_sum - smallest_difference

