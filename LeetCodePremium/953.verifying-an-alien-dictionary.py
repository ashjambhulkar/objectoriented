#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        result = collections.defaultdict(int)
        for i in range(len(order)):
            result[order[i]] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if result[word2[j]] < result[word1[j]]:
                        return False
                    break
                   
            if len(word1) > len(word2):
                return False

        return True

            
        
# @lc code=end

