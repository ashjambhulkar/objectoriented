#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start

# Time O(NogN)
# Space O(N)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lheap, rheap = [], []
        result = 0
        start = 0
        for end, value in enumerate(nums):
            heapq.heappush(lheap, (value, end))
            heapq.heappush(rheap, (-value, end))
            while -rheap[0][0]-lheap[0][0] > limit:
                start = min(lheap[0][1], rheap[0][1])+1
                while start > lheap[0][1]:
                    heapq.heappop(lheap)
                while start > rheap[0][1]:
                    heapq.heappop(rheap)
            result = max(result, end-start+1)
        return result


# @lc code=end

