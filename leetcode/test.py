class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
  def deleteNode(self, root, val):
    if not root:
      return None
    
    if root.val > val:
      root.left = self.deleteNode(root.left, val)
    elif root.val < val:
      root.right = self.deleteNode(root.right, val)
    else:
      if not root.left and not root.right:
        root = None
      elif root.right:
        root.val = self.successor(root)
        root.right = self.deleteNode(root.right, root.val)
      else:
        root.val = self.predecessor(root)
        root.left = self.deleteNode(root.left, root.val)
    return root
  
  def successor(self, root):
    root = root.right
    while root.left:
      root = root.left
    return root.val

  def predecessor(self, root):
    root = root.left
    while root.right:
      root = root.right
    return root.val
	
  
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sample = Solution().deleteNode(root, 2)
def helper(sample):
	if not sample:
		return 
	helper(sample.left)
	print(sample.val)
	helper(sample.right)
helper(sample)

