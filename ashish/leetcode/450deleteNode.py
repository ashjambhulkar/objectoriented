# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference(possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5, 3, 6, 2, 4, null, 7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7


def successor(root):
  root = root.right
  while root.left:
    root = root.left
  return root.val

def predecessor(root):
  root = root.left
  while root.right:
    root = root.right
  return root.val

def deleteNode(root, key):
  if not root:
    return None
  
  if key > root.val:
    root.right = deleteNode(root.right, key)
  elif key < root.val:
    root.left = deleteNode(root.left, key)
  else:
    if not root.right and not root.left:
      root = None
    elif root.right:
      root.val = successor(root)
      root.right = deleteNode(root.right, root.val)
    else:
      root.val = predecessor(root)
      root.left = deleteNode(root.left, root.val)
  return root

