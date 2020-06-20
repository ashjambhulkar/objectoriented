#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        string = sentence.split()
        for i in range(len(string)):
            temp = ""
            for ch in string[i]:
                temp += ch
                if temp in dict:
                    break
            string[i] = temp
        return " ".join(string)
                
        ## Implement Trie Way
        
# @lc code=end

