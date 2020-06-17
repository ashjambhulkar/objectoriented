# Given the root node of a binary search tree(BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.



def searchBST(root, val):
  if not root:
    return None
  if val > root.val:
    return searchBST(root.right, val)
  elif val < root.val:
    return searchBST(root.left, val)
  else:
    return root