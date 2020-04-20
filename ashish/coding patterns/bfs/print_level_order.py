# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.


from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None


def helper(root):
  result = []
  if not root:
    return result
  queue = deque()
  queue.append(root)
  while queue:
    temp = []
    for _ in range(len(queue)):
      node = queue.popleft()
      
