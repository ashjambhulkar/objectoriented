#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []

        for x in points:
            heapq.heappush(result, (x[0]**2 + x[1]**2, x))

        answer = []
        for _ in range(K):
            _, values = heapq.heappop(result)
            answer.append(values)
        return answer
# @lc code=end

