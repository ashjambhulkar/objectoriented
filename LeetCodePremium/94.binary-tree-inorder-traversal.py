#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(n) | O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # self.result = []
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     self.result.append(root.val)
        #     helper(root.right)
        # helper(root)
        # return self.result
        if not root:
            return []
        stack = []
        result = []
        
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                temp = stack.pop()
                result.append(temp.val)
                root = temp
                root = root.right
            else:
                break
        return result



        
# @lc code=end

