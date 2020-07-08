#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

import collections


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)

        for x in prerequisites:
            graph[x[1]].append(x[0])

        def depthfirstsearch(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for x in graph[i]:
                if not depthfirstsearch(x):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not depthfirstsearch(i):
                return False
            return True
       
print(Solution().canFinish(3,[[1,0],[2,0],[3,2],[3,1]]))

           
# @lc code=end

