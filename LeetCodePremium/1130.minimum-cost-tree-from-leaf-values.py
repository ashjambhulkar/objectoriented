#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
# O(N^2) | O(N)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total = 0
        while len(arr) > 1:
            index = arr.index(min(arr))
            total += min(arr[index-1:index]+arr[index+1:index+2]) * arr.pop(index)
        return total
        

        
# @lc code=end

