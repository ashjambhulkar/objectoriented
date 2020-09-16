#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for x, y in tickets:
            graph[x].append(y)
        
        for x in graph:
            graph[x].sort()
        result = []
        def helper(root):
            while graph[root]:
                x = graph[root].pop(0)
                helper(x)
            result.append(root)
        helper("JFK")
        return result[::-1]

        
# @lc code=end

