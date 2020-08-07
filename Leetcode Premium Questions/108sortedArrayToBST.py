# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10, -3, 0, 5, 9],

# One possible answer is: [0, -3, 9, -10, null, 5], which represents the following height balanced BST:

#### Note

# It's known that inorder traversal of BST is an array sorted in the ascending order.

# Having sorted array as an input, we could rewrite the problem as Construct Binary Search Tree from Inorder Traversal.

# Does this problem have a unique solution, i.e. could inorder traversal be used as a unique identifier to encore/decode BST? The answer is no.
# Here is the funny thing about BST. Inorder traversal is not a unique identifier of BST. At the same time both preorder and postorder traversals are unique identifiers of BST. From these traversals one could restore the inorder one: inorder = sorted(postorder) = sorted(preorder), and inorder + postorder or inorder + preorder are both unique identifiers of whatever binary tree.

class TreeNode(object):
  pass

def solution(nums):
  def helper(left, right):
    if left > right:
      return
    mid = (left+right) // 2
    root = TreeNode(nums[mid])
    root.left = helper(left, mid-1)
    root.right = helper(mid+1, right)
    return root
  return helper(0, len(nums)-1)
