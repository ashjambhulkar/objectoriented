#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.all(root) 

    def all(self, root):
        if not root:
            return
        self.all(root.left)
        self.stack.insert(0,root.val)
        self.all(root.right)
 
    def next(self) -> int:
        return self.stack.pop()

        
    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

