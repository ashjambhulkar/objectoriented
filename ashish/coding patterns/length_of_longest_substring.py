# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# Input: String = "aabccbb", k = 2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

def helper(string, k):
  if not string:
    return 0
  start = 0
  count = 0
  length = 0
  result = {}
  for end in range(len(string)):
    end_char = string[end]
    if end_char not in result:
      result[end_char] = 0
    result[end_char] += 1
    count = max(count, result[end_char])
    if (end-start+1  - count) > k:
      start_char = string[start]
      result[start_char] -= 1
      start += 1
    length = max(length, end-start+1)
  return length

string = "bbasef"
k = 2
print(helper(string, k))