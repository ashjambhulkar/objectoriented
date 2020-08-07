#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time O(n) | Space O(n)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # Recursive solution
        # self.result = []
        # def helper(root):
        #     if not root:
        #         return 
        #     self.result.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return self.result

        # Iterative Solution
        if not root:
            return []

        stack = []
        result = []
        while True:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            elif stack:
                temp = stack.pop()
                root = temp.right
            else:
                break

        return result
        
# @lc code=end

