#First we will create a treenode class to create the binary search tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def helper(self, root):
    #left value is -ve infinity and right value is +ve infinity we will update this value and check whether the left value or right value is in between the actual left and right value.
    stack = [(root, float("-inf"), float("inf")),]
    #iterative way
    while stack:
      node, left, right = stack.pop()
      if not node:
        continue
      if node.val <= left or node.val >= right:
        return False
      stack.append((node.right, node.val, right))
      stack.append((node.left, left, node.val))
    return True

  def recursive(self, root):
    def result(root, left, right):
      if not root:
        return True
      if root.val <= left or root.val >= right:
        return False
      return result(root.left, left, root.val) and result(root.right, root.val, right)
    return result(root, float("-inf"), float("inf"))


