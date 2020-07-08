#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        test = set(words)
        result = []
        for x in words:
            start = 0
            count = 0
            for end in range(len(x)):
                if x[start:end+1] in test:
                    start = end+1
                    count += 1
            if count > 1:
                result.append(x)
        return result
# @lc code=end

