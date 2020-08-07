#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftmax, rightmax = 0, 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    result += (leftmax - height[left])
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    result += rightmax - height[right]
                right -= 1
        return result
            
# @lc code=end


