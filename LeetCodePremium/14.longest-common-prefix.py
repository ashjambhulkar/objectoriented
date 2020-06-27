#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        result = ""
        for i in range(1, len(strs)):
            test = ""
            for j in range(len(sample)):
                if strs[j] == sample[j]:
                    test += strs[j]
                else:
                    break
        return test
        




        
# @lc code=end

