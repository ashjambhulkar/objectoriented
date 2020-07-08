#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.childern = collections.defaultdict(TrieNode)
        self.sample = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        result = []
        for x in products:
            current = root
            for char in x:
                current = current.childern[char]
                current.sample.append(x)
                current.sample.sort()
                if len(current.sample) > 3:
                    current.sample.pop()
        current = root
        for char in searchWord:
            current = current.childern[char]
            result.append(current.sample)
                    
        return result
        
# @lc code=end

