#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        sample = collections.defaultdict(list)
        for x, y in edges:
          sample[x].append(y)
          sample[y].append(x)
        result = [0] * N
        for i in range(N):
          queue = collections.deque([(i, 0)])
          visited = {i}
          while queue:
            node, depth = queue.popleft()
            result[i] += depth
            for x in sample[node]:
              if x not in visited:
                visited.add(x)
                queue.append((x, depth+1))
        return result
        
# @lc code=end

