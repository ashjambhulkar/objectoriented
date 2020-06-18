


#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        percent = 100/len(arr)
        result = -1
        for x in arr:
            hashmap[x] += percent
            if hashmap[x] > 25:
                result = x
        return result
# @lc code=end

