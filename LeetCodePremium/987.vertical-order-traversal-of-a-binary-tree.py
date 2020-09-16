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
        def helper(root, row, depth):
            nonlocal result
            if not root:
                return 
            result[depth].append((row, root.val))
            helper(root.left, row+1, depth-1)
            helper(root.right, row+1, depth+1)
        helper(root, 0, 0)
        temp = []
        for x in sorted(result):
            temp.append([])
            [temp[-1].append(y) for x, y in sorted(result[x])]
        return temp




# @lc code=end

