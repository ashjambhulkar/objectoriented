#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #find the peak in the mountain arr
        size = mountain_arr.length()
        l, r = 0, size-1
        while l < r:
            m = (l+r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m+1
            else:
                r = m
        peak = l

        #find the target in the left of the peak
        l, r = 0, peak
        while l < r:
            m = (l+r) // 2
            if mountain_arr.get(m) == target:
                return m
            if mountain_arr.get(m) < target:
                l = m+1
            else:
                r = m-1

        #find the target in the right of the peak
        l, r = peak, size-1
        while l < r:
            m = (l+r) // 2
            if mountain_arr.get(m) == target:
                return m
            if mountain_arr.get(m) > target:
                l = m+1
            else:
                 r = m-1
        return -1
# @lc code=end

