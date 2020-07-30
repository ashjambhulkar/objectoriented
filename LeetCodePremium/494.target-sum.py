#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        result = collections.defaultdict(int)
        result[0] = 1
        for x in nums:
            sample = collections.defaultdict(int)
            for y in result:
                sample[y+x] += result[y]
                sample[y-x] += result[y]
            result = sample
        return result[S]


# @lc code=end

