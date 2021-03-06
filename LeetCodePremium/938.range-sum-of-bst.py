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
        total = 0 
        def helper(root):
            nonlocal total
            if not root:
                return
            helper(root.left)
            if L <= root.val <= R:
                total += root.val
            helper(root.right)
        helper(root)
        return total
        
# @lc code=end

