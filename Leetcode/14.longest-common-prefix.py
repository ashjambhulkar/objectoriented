#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(result) < 1:
                break
            for j in range(len(strs[i])):
                if result[j] == strs[i][j]:
                    temp += result[j]
                else:
                    break
            if len(temp) < len(result):
                result = temp
        return result

       
# @lc code=end

