#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # Time O(N ^ 2)
        # Space O(N)
        result = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            result += min(arr[i-1:i]+arr[i+1:i+2]) * arr.pop(i)
        return result

        
# @lc code=end

