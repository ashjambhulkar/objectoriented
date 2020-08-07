#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.total = float("-inf")
        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            self.total = max(self.total, left+right+root.val)
            return max(left+root.val, right+root.val, 0)
        helper(root)
        return self.total
# @lc code=end

