#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = float("-inf")
        result = ""
        for end in range(len(s)):
            start = 0
            while start <= end:
                if end-start+1 > len(result):
                    temp = s[start:end+1]
                    if temp == temp[::-1]:
                        if count < end-start+1:
                            count = end-start+1
                            result = temp
                start += 1
        return result


# @lc code=end

