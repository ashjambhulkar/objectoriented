#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # self.deepest, self.lca = 0, None
        # def helper(root, depth):
        #     self.deepest = max(self.deepest, depth)
        #     if not root:
        #         return depth
        #     left = helper(root.left, depth+1)
        #     right = helper(root.right, depth+1)
        #     if left == right == self.deepest:
        #         self.lca = root
        #     return max(left, right)
        # helper(root, 0)
        # return self.lca

        def helper(root):
            if not root:
                return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2:
                return h1+1, lca1
            if h2 > h1:
                return h2+1, lca2
            return h1+1, root
        return helper(root)[1]
        
# @lc code=end

