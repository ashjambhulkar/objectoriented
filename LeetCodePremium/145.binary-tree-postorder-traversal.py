#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

\
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) | O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # self.result = []
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     helper(root.right)
        #     self.result.append(root.val)
        # helper(root)
        # return self.result

        if not root:
            return []
        
        result = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                temp = stack.pop()
                root = temp.right
                result.append(temp.val)
            else:
                break
        return result


        
# @lc code=end

