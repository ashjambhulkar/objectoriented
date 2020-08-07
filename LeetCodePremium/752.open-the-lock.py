#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque([("0000", 0)])
        visited = set([("0000")])

        def neighbors(node):
          for i in range(4):
            x = int(node[i])
            for y in [1, -1]:
              temp = (x+y) % 10
              yield node[:i] + str(temp) + node[i+1:]

        while queue:
          node, depth = queue.popleft()
          if node == target:
            return depth
          if node in deadends:
            continue
          for nei in neighbors(node):
            if nei not in visited:
              visited.add(nei)
              queue.append((nei, depth+1))
        return -1
        
# @lc code=end

