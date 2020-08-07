
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Iterative
# def traverse(root):
#   result = []
#   if not root:
#     return result
#   queue = deque()
#   queue.append(root)
#   while queue:
#     temp = []
#     for _  in range(len(queue)):
#       node = queue.popleft()
#       temp.append(node.val)
#       if node.left:
#         queue.append(node.left)
#       if node.right:
#         queue.append(node.right)
#     result.append(temp)
#   return result


# recursive
def traverse(root, depth=0, result=[]):
  if not root:
    return
  if len(result) == depth:
    result.append([])

  result[depth].append(root.val)
  if root.left:
    traverse(root.left, depth+1)
  if root.right:
    traverse(root.right, depth+1)
  return result
    




def helper():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))
    
helper()
    
