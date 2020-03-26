# Given a string and a pattern, find all anagrams of the pattern in the given string.
# Input: String = "ppqp", Pattern = "pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

def helper(string, pattern):
  start = 0
  result = {}
  test = []
  match = 0
  for i in range(len(pattern)):
    result[pattern[i]] = 1
  
  for end in range(len(string)):
    end_char = string[end]
    if end_char in result:
      result[end_char] -= 1
ZZs      if result[end_char] == 0:
        match += 1
  
    if match == len(pattern):
      test.append(start)

    if end > len(pattern)-1:
      start_char = string[start]
      start += 1
      if start_char in result:
        if result[start_char] == 0:
          match -= 1
        result[start_char] += 1
  return test


string = "abbcabc"
pattern = "abc"
print(helper(string, pattern))
