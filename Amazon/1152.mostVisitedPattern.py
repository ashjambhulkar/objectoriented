import  heapq
import collections
import combination

def mostVisitedPattern(self, username, timestamp, website):
  queue = []
  queue = []
  heapq.heapify(queue)
  #1) sort data based on timestamp - O(logn) where n = number of users
  for uname, tstamp, wsite in zip(username, timestamp, website):
      heapq.heappush(queue, (tstamp, wsite, uname))

  user_dict = collections.defaultdict(list)
  #2) categorize websites based on users - O(n)
  while queue:
      _, web, user = heapq.heappop(queue)
      user_dict[user].append(web)

  seq_count_dict = collections.defaultdict(int)
  max_count = 0
  result = tuple()

  #3) traverse thriugh all websites to fins sequence of 3 - O(n*k)
  for websites in user_dict.values():
      # O(k^3) where k is max number of websites visted by a user
      seq_combinations = combinations(websites, 3)

      # since we want the count of a sequence visited by most number of users, if a user visits the same sequence multiple times, it is counted as 1
      for seq in set(seq_combinations):
          seq_count_dict[seq] += 1

          if seq_count_dict[seq] > max_count:
              max_count = seq_count_dict[seq]
              result = seq
          # If the count is same and you find a sequence with a smaller lexographical order
          elif seq_count_dict[seq] == max_count:
              if seq < result:
                  result = seq
  return list(result)
  #Time Complexity: O(n*k^3)
