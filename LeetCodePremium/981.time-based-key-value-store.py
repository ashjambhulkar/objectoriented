#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
import collections
class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        test = self.hashmap[key]
        if test[0][1] > timestamp:
            return ""
        i, j = 0, len(test)
        -1
        while i < j:
            # mid = test[i][1]+test[j][1]
            mid = (i + j)//2
            if test[mid][1] <= timestamp:
                i = mid+1
            else:
                j = mid
        return test[j-1
        ][0]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
