#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, left=float("-inf"), right=float("inf")):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        return helper(root)
        
# @lc code=end

