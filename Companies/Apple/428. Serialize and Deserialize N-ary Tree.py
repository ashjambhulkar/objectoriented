import collections

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Codec:
  def serialize(self, root):
    result = []
    def preorder(root):
      if not root:
        return

      result.append(str(root.val))
      for child in root.childrens:
        preorder(child)
      result.append('#')
    preorder(root)
    return " ".join(result)

  def deserialize(self, data):
    if not data:
      return None
    
    tokens = collections.deque(data.split())
    root = Node(int(tokens.popleft()), [])
    
    def helper(node):
      if not tokens:
        return 

      while tokens[0] != "#":
        value = tokens.popleft()
        child = Node(int(value), [])
        node.children.append(child)
        helper(child)
      tokens.popleft()

    helper(root)
    return root



