#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            current = current.children[ch]
        current.end = True
        

    def search(self, word: str) -> bool:
        current = self.root
        self.result = False
        self.dfs(current, word)
        return self.result

    def dfs(self, node, word):
        if not word:
            if node.end:
                self.result = True
        
            return

        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

