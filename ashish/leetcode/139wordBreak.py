import collections
def helper(word, wordlist):
  queue = collections.deque()
  queue.append(0)
  visited = set()
  visited.add(0)
  while queue:
    start = queue.popleft()
    for i in range(start, len(word)+1):
      if i in visited:
        continue
      if word[start:i] in wordlist:
        if i == len(word):
          return True
        queue.append(i)
        visited.add(i)

  return False

word = "applepenappl"
wordlist = ["apple", "pen"]
print(helper(word, wordlist))
