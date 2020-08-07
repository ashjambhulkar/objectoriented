def max_path(root):
  total = float("-inf")
  def helper(node):
    nonlocal total
    if not node:
      return 0
    left_total = max(helper(node.left), 0)
    right_total = max(helper(node.right), 0)
    full_total = node.val + left_total + right_total
    total = max(total, full_total)
    return node.val + max(left_total, right_total)
  helper(root)
  return total
