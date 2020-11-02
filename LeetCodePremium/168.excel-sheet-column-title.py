#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n):
        result = ""
        carry = n
        while carry > 26:
            value, carry = divmod(n, 26)
            result += chr(value+64)
        if carry > 0:
            result += chr(carry+64)
        return result

Solution().convertToTitle(52)
# @lc code=end

