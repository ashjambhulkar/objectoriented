#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        def helper(low=0, high=len(nums)-1):
            if low > high:
                return None
            mid = low + (high-low)//2
            root = TreeNode(nums[mid])
            root.left = helper(low, mid-1)
            root.right = helper(mid+1, high)
            return root
        return helper()


        
# @lc code=end

