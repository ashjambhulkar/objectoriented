#Given a string, find the length of the longest substring in it with no more than K distinct characters.

# def helper(string, k):
#   if len(string) < 2:
#     return min(len(string), k)
#   start = 0
#   result = 0
#   for end in range(len(string)):
#     temp = string[start:end]
#     if len(set(list(temp))) >= k:
#       result = max(result, end-start+1)
#       start +=1
#   return result

def helper(string, k):
  hashmap = {}
  start = 0 
  result = 0 
  for end in range(len(string)):
    charecter = string[end]
    if charecter not in hashmap:
      hashmap[charecter] = 0
    hashmap[charecter] += 1
    while len(hashmap) > k:
      start_char = string[start]
      hashmap[start_char] -= 1
      if hashmap[start_char] == 0:
        del hashmap[start_char]
      start += 1
    result = max(result, end-start+1)
  return result
  


string = "cbbebi"
k = 3
print(helper(string, k))
