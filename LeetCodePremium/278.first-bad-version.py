#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right) // 2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid-1
        return left
                

        
        

# @lc code=end

