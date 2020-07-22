#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = collections.defaultdict(list)
        left, right = float("inf"), float("-inf") 
        def helper(root, row, col):
            nonlocal left, right
            if not root:
                return
            
            result[col].append((row, root.val))
            left = min(left, col)
            right = max(right, col)
            helper(root.left, row+1, col-1)
            helper(root.right, row+1, col+1)
        helper(root, 0, 0)
        final = []
        count = 0
        for i in range(left, right+1):
            result[i].sort()
            final.append([])
            for x in result[i]:
                key, value = x
                final[count].append(value)
            count += 1
        return final
# @lc code=end

