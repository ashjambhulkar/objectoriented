#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value =  0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key = []
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for ch in key:
            current = current.children[ch]
            if key in self.key:
                current.value = val
            else:
                current.value += val
        self.key.append(key)

    def sum(self, prefix: str) -> int:
        current = self.root
        for ch in prefix:
            current = current.children.get(ch)
            if not current:
                return 0
        return current.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

