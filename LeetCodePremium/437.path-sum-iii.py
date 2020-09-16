#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sample = collections.defaultdict(int)
        count = 0
        def preorder(root, total):
            nonlocal count
            if not root:
                return 
            total += root.val
            if total == sum:
                count += 1
            
            count += sample[total-sum]
            sample[total] += 1
            preorder(root.left, total)
            preorder(root.right, total)
            sample[total] -= 1
        preorder(root, 0)
        return count
# @lc code=end

