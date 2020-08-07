
from collections import defaultdict, Counter, deque


def alienOrder(self, words: List[str]) -> str:
  result = collections.defaultdict(set)
  in_degree = collections.defaultdict(int)

  for word in words:
    for c in word:
      in_degree[c] = 0
  
  for i in range(1, len(words)):
    first = words[i-1]
    second = words[i]
    for j in range(min(len(first), len(second))):
      if first[j] != second[j]:
        if second[j] not in result[first[j]]:
          result[first[j]].add(second[j])
          in_degree[second[j]] += 1
          break
      else:
        if len(first) > len(second):
          return ""
        
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else:  # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word):
                return ""

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)
