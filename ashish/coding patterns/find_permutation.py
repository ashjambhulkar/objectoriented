# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Input: String = "oidbcaf", Pattern = "abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

def helper(string, pattern):
  start = 0
  result = {}
  match = 0
  for i in range(len(pattern)):
    result[pattern[i]] = 1
  
  for end in range(len(string)):
    end_char = string[end]
    if end_char in result:
      result[end_char] -= 1
      if result[end_char] == 0:
        match += 1

    if match == len(pattern):
      return True
    
    if end > len(pattern) - 1:
      start_char = string[start]
      start += 1
      if start_char in result:
        if result[start_char] == 0:
          match -= 1
        result[start_char] += 1
  return False


string = "aacab"
pattern = "abc"
print(helper(string, pattern))
