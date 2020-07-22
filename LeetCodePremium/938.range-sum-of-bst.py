#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        def helper(root):
            if not root:
                return
            helper(root.left)
            if root.val >= L and root.val <= R:
                self.total += root.val
            helper(root.right)
        helper(root)
        return self.total
        
# @lc code=end

