class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
  def helper(self, root):
    stack = [(root, float("-inf"), float("inf")),]
    while stack:
      node, left, right = stack.pop()
      if not node:
        continue
      if node.val <= left or node.val >= right:
        return False
      stack.append((node.right, node.val, right))
      stack.append((node.left, left, node.val))
    return True
