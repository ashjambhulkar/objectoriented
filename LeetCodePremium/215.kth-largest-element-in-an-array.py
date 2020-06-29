#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for x in nums:
            heapq.heappush(result, -x)
        
        for i in range(k-1):
            heapq.heappop(result)

        return -heapq.heappop(result)


        
# @lc code=end

