#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = 0, len(height)-1
        # result = 0
        # while left < right:
        #     if height[left] < height[right]:
        #         result = max(result, height[left] * (right-left))
        #         left += 1
        #     else:
        #         result = max(result, height[right] * (right-left))
        #         right -= 1
        # return result


        result = 0
        low = 0
        high = len(height)-1
        while low < high:
            result = max(min(height[low], height[high]) * (high-low), result)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return result


        
# @lc code=end

