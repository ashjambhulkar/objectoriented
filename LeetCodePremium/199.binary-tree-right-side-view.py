#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.result  = []

        def helper(root, depth):
            if not root:
                return
            if depth == len(self.result):
                self.result.append([])
            self.result[depth].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0
        )
        final = []
        for x in self.result:
            final.append(x[-1])
        return final

            
        
# @lc code=end

