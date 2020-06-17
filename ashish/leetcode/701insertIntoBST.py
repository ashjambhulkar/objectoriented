# Given the root node of a binary search tree(BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
  def __init__(self, val):
    self.val = val

def insertIntoBST(root, val):
  if not root:
    return TreeNode(val)
  if val > root.val:
    root.right = insertIntoBST(root.right, val)
  else:
    root.right = insertIntoBST(root.left, val)
  return root
