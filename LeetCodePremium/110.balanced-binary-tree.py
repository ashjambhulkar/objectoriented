#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        def helper(root):
            if not root or not self.balanced:
                return -1
            l = helper(root.left)
            r = helper(root.right)
            if abs(l-r) > 1:
                self.balanced = False
                return -1
            return max(l, r) + 1
        helper(root)
        return self.balanced
        
# @lc code=end

