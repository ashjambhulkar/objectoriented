#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        temp = numerator / denominator
        result = str(temp).split(".")
        print(result)
                
# @lc code=end

