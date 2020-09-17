#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # hashset = set(wordDict)
        # result = collections.defaultdict(list)
        # def helper(s):
        #     if not s:
        #         return [[]]
            
        #     if s in result:
        #         return  result[s]

        #     for end in range(1, len(s)+1):
        #         if s[:end] in hashset:
        #             for temp in helper(s[end:]):
        #                 result[s].append([s[:end]]+temp)
        #     return result[s]
        
        # helper(s)

        # return [" ".join(words) for words in result[s]]


        # sample = set(wordDict)
        # result = []
        
        # def helper(start, string, temp):
        #     if len(string) == 0:
        #         result.append(temp.strip())
        #         return
        #     for i in range(len(string)):
        #         if string[:i+1] in sample:
        #             helper(i+1, string[i+1:], temp + string[:i+1] + " ")
        # helper(0, s, "")
        # return result


        result = []
        def helper(string, start, temp):
            if len(string) == 0:
                result.append(temp[:].strip())
                return 
            for i in range(len(string)):
                if string[:i+1] in wordDict:
                    helper(string[i+1:], i+1, temp +string[:i+1]+" ")
        helper(s, 0, "")
        return result

# @lc code=end

