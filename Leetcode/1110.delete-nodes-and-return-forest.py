#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        hashset = set(to_delete)
        result = []
        def helper(root, parent):
            if not root:
                return
            if root.val in hashset:
                root.left = helper(root.left, False)
                root.right = helper(root.right, False)
                return None
            else:
                if not parent:
                    result.append(root)
                root.left = helper(root.left, True)
                root.right = helper(root.right, True)
                return root
        helper(root, False)
        return result

#here the first return None is actually returning the none to divide the tree as it will not return the root whereas the second return is actually returning the root to create the tree. if  root.val is in hashset then we are saying that both the child does not have the parent and can be treated as differetn tree.
# @lc code=end

