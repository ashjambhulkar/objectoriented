#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        ## O(NlogN) | O(N)
        # inorder = sorted(preorder)
        # def helper(left, right):
        #     if left > right:
        #         return None
            
        #     val = preorder.pop(0)
        #     root = TreeNode(val)
        #     index = inorder.index(val)
        #     root.left = helper(left, index-1)
        #     root.right = helper(index+1, right)
        #     return root
        # return helper(0, len(inorder)-1)
        
        # O(N) | O(N)
        count = 0
        size = len(preorder)
        def helper(left=float("-inf"),right=float("inf")):
            nonlocal count
            if count == size:
                return None
            val = preorder[count]
            if val < left or val > right:
                return None
            root = TreeNode(val)
            count += 1
            root.left = helper(left, val)
            root.right = helper(val, right)
            return root
        return helper()

        
# @lc code=end

