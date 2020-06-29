#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        start = 0
        for end in range(len(s)):
            if self.checkpalindrom(s[start:end+1]):
                if len(result) < end-start+1:
                    result = s[start:end+1]
                else:
                    temp = start
                    while temp < end:
                        if end-temp+1 > len(result):
                            result = s[temp:end+1]
                        temp += 1
                    start += 1
        return result

    def checkpalindrom(self, string):
        left = 0 
        right = len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
# @lc code=end

