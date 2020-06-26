#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left) and left.val == right.val
        return helper(root.left, root.right)
    
# @lc code=end

