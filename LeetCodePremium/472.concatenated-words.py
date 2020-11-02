#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.result = []
        self.words = set(words)
        for word in words:
            if self.dfs(word):
                self.result.append(word)
        return self.result


    def dfs(self, word):
        for i in range(1, len(word)):
            left = word[0:i]
            right = word[i:]

            if left in self.words and right in self.words:
                return True
            if left in self.words and self.dfs(right):
                return True
            if right in self.words and self.dfs(left):
                return True
        return False

        
# @lc code=end



