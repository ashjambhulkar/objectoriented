#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hashset = set(wordDict)
        result = collections.defaultdict(list)
        def helper(s):
            if not s:
                return [[]]
            
            if s in result:
                return  result[s]

            for end in range(1, len(s)+1):
                if s[:end] in hashset:
                    for temp in helper(s[end:]):
                        result[s].append([s[:end]]+temp)
            return result[s]
        
        helper(s)

        return [" ".join(words) for words in result[s]]

# @lc code=end

