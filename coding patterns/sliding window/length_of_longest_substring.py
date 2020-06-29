# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# Input: String = "aabccbb", k = 2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

import collections


def helper(string, k):
  hashmap = collections.defaultdict(int)
  result = float("-inf")
  start = 0
  for end in range(len(string)):
    end_char = string[end]
    hashmap[end_char] += 1
    if len(hashmap) == k:
      result = max(result, end-start+1)

    while len(hashmap) > k:
      start_char = string[start]
      hashmap[start_char] -= 1
      if hashmap[start_char] == 0:
        del hashmap[start_char]
      start += 1

  return result

string = "bbasef"
k = 2
print(helper(string, k))
