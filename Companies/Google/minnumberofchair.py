import heapq
def helper(s, e):
  if len(s) != len(e) or not (s or e):
    return 0
  result = []
  for i in range(len(s)):
    result.append([s[i],e[i]])
  result.sort(key=lambda x:x[0])
  ###answer using heap memory

  # sample = []
  # heapq.heappush(sample, result[0][1])

  # for x in result[1:]:
  #   if sample[0] <= x[0]:
  #     heapq.heappop(sample)
  #   heapq.heappush(sample, x[1])
  
  # return len(sample)

  ### answer using two pointers
  # all = [(x, 1) for x in s] + [(y, -1) for y in e]
  # all.sort()
  # print(all)
  # num = 0
  # largest = 0
  # for x, y in all:
  #   num += y
  #   if largest < num:
  #     largest = num
  # return largest



S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
print(helper(S,E))

