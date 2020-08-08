#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using two pointers to track the low and high of inorder, the taking last element from postorder as the last element is the root element. Therefore building the righ tree first till the last both child None and the retracting the pointer back to create the left subtree. The reason to build right subtree is because the post order works in left->right->root therfore the root created first and then right subtree and then left subtree.
# O(N) | O(N)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(low, high):
            if low > high:
                return None
            
            val = postorder.pop()
            index = inorder.index(val)
            root = TreeNode(val)
            root.right = helper(index+1, high)
            root.left = helper(low, index-1)
            return root
        return helper(0, len(inorder)-1)

        
        
# @lc code=end

