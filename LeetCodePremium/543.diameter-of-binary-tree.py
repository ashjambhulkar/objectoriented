#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0 
        self.answer = 1
        def helper(root):
            if not root:
                return 0
            left  = helper(root.left)
            right = helper(root.right)
            self.answer = max(self.answer, left+right+1)
            return max(left,right) + 1
        return self.answer-1
            
        
# @lc code=end

