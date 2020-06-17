# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# The successor of a node p is the node with the smallest key greater than p.val.

# Example 1:

# Input: root = [2, 1, 3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

## The concept here is binary search tree left value is always less that root and right value

class TreeNode(object):
  pass


def helper(root, p):
  result = TreeNode(None)
  while root:
    # we need to find the next big value than the p.val therefore we are checking this condition
    if root.val <= p.val:
      root = root.right
    else:
      result = root
      root = root.left
  return result
