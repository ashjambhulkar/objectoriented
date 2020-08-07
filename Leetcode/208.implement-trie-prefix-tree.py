#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            current = current.children[ch]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            current = current.children.get(ch)
            if not current:
                return False
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            current = current.children.get(ch)
            if not current:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

