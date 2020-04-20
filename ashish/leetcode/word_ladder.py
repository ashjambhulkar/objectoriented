from collections import defaultdict, deque


def helper(begin, end, wordlist):
	if end not in wordlist or not wordlist or not end or not begin:
		return 0
	
	temp = defaultdict(list)
	for word in wordlist:
    for i in range(len(endword)):
      temp[word[:i] + "*" + word[i+1:]].append(word)
  
  queue = deque()
	queue.append((begin, 1))
	visited = {begin: True}
	while queue:
		node, depth = queue.popleft()
		for i in range(len(begin)):
			middle_word = node[:i] + "*" + node[i+1:]
			for x in temp[middle_word]:
				if x is end:
					return depth
				if x not in visited:
					visted[x] = True
					queue.append((x, depth+1))
	return 0
