#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # if not root:
        #     return False
        # def helper(root, sum):
        #     if not root:
        #         return 
        #     sum -= root.val
        #     if not root.left and not root.right:
        #         return sum == 0
        #     return helper(root.left, sum) or helper(root.right, sum)
        # return helper(root, sum)


        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

        
# @lc code=end

