# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right 
# in separate sub-arrays.


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  

def helper(root):
  if not root:
    return 
  

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))

main()