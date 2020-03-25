# Given a string, find the length of the longest substring which has no repeating characters.
# Input: String = "aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

def non_repeat_substring(string):
  start = 0
  count = 0
  result = set()
  for end in range(len(string)):
    end_char = string[end]
    if end_char not in result:
      result.add(end_char)
      count = max(count, end-start+1)
    else:
      result = set()
      result.add(end_char)
      start = end
  return count


string = "abccba"
print(non_repeat_substring(string))


