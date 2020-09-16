count = 0
def helper(root):
  # nonlocal count
  if not root.left and not root.right:
    count += 1
    return True
  status = True
  if root.left:
    status = helper(root.left) and root.val == root.left.val
  
  if root.right:
    helper(root.right) and root.val == root.right.val and status
  
  return status