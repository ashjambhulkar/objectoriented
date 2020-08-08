#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = collections.Counter(p)
        sdict = collections.Counter(s[:len(p)])
        start = 0
        end = len(p)
        result = []
        while end <= len(s):
            if pdict == sdict:
                result.append(start)
            
            sdict[s[start]] -= 1
            if sdict[s[start]] <= 0:
                sdict.pop(s[start])
            
            if end < len(s):
                sdict[s[end]] += 1
            end += 1
            start += 1

        return result
       
# @lc code=end

