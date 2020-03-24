#Given a string, find the length of the longest substring in it with no more than K distinct characters.

def helper(string, k):
  start = 0
  result = 0
  for end in range(len(string)):
    temp = string[start:end]
    if temp

string = "araaci"
k = 2
print(helper(string, k))
