#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)
        
        for x in prerequisites:
            graph[x[1]].append(x[0])
        
        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = -1
            for x in graph[i]:
                if not dfs(x):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            return True
  

# @lc code=end

