#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        def helper(root, depth=0):
            if not root:
                return
            if len(self.result) == depth:
                self.result.append([])
            self.result[depth].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root)
        for x in range(len(self.result)):
            if x %2 != 0:
                self.result[x].reverse()
        return self.result
        
# @lc code=end

