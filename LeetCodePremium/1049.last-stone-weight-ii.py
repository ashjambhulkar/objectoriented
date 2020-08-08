#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones):
        dp = {0}
        for a in stones:
            dp = {a-i for i in dp} | {a+i for i in dp}
        return min(abs(x) for x in dp)


        
# @lc code=end

