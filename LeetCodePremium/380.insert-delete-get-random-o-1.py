#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start

class RandomizedSet:

    def __init__(self):
        self.hashmap = collections.defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(arr)
            self.arr.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        del self.hashmap[val]
        self.hashmap[temp] = self.arr[-1]
        self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
        self.arr.pop
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

