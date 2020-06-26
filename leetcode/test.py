import collections

def maxArea(s, t):
  start = 0
  string = ""
  count = float("inf")
  hashmap = collections.Counter(list(t))
  for end in range(len(s)):
    end_char = s[end]
    if end_char in hashmap:
      hashmap[end_char] -= 1
      if hashmap[end_char] == 0:
        del hashmap[end_char]
    if len(hashmap) == 0:
      if end-start+1 < count:
        string = s[start:end+1]
        count = end-start+1
        start = end+1
        hashmap = collections.Counter(list(t))
        while start < len(s):
          if s[start] in hashmap:
            break
          start += 1
  return string


s = "ADOBECODEBANC"
t = "DEA"

print(maxArea(s, t))
