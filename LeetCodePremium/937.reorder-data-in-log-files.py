#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digits = []
        for x in logs:
            if x.split()[1].isdigit():
                digits.append(x)
            else:
                letter.append(x)
        # when suffix is tie, sort by identifier
        letter.sort(key = lambda x:x.split()[0])
        # sort by suffix
        letter.sort(key = lambda x:x.split()[1:])
        return letter+digits


        
# @lc code=end

