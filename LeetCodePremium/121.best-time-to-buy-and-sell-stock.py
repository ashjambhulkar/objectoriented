#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = float("inf")
        end = float("-inf")
        left = 0
        right = len(prices)-1
        while left < right:
            
        
# @lc code=end

