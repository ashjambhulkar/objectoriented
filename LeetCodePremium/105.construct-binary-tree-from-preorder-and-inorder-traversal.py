#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        print(len(inorder))
        def helper(low, high):
            if low > high:
                return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            index = inorder.index(val)

            root.left = self.buildTree(low, index-1)
            root.right = self.buildTree(index+1, high)
            return root

        helper(0, len(inorder)-1)
# @lc code=end

