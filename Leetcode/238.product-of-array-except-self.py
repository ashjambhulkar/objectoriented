#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        result = list()
        for i in range(len(nums)-1):
            left.append(left[i]*nums[i])
        
        for i in range(len(nums)-1,0,-1):
            right.insert(0, right[0] * nums[i])
        
        for i in range(len(nums)):
            result.append(left[i]*right[i])

        return result


        # p = 1
        # n = len(nums)
        # result = []
        # for i in range(n):
        #     result.append(p)
        #     p *= nums[i]
        # p = 1
        # for i in range(n):
        #     result[i] *= p
        #     p *= nums[i]

        # return result

        
# @lc code=end

