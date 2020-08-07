#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        result = 0
        for word in words:
            i = 0
            j = 0
            while i < len(S) and j < len(word):
                if S[i] != word[j]:
                    break
                left = 1
                right = 1
                while i+1 < len(S) and S[i] == S[i+1]:
                    i += 1
                    left += 1
                while j+1 < len(word) and word[j] == word[j+1]:
                    j += 1
                    right += 1

                if left < right or (left > right and left < 3):
                    break
                
                i += 1
                j += 1
                
                if i == len(S) and j == len(word):
                    result += 1
        return result

        
# @lc code=end

