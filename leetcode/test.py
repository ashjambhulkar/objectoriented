class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right



def insert_node(root, val, parents):
    if not root:
        return TreeNode(val)

    parents[val].append(root)

    if root.val < val:
        root.right = insert_node(root.right, val, parents)
    else:
        root.left = insert_node(root.left, val, parents)

    return root

def bstDistance(num, values, node1, node2):
    if not values or node1 not in values or node2 not in values:
        return -1
    if node1 == node2:
        return 0 
        
    parents = {}
    
    for num in values:
        parents[num] = []
    
    root = TreeNode(values[0])
    
    #construct BST
    for i in range(1, len(values)):
        insert_node(root, values[i], parents)
        
    # calculate Distance
    parent_node1 = parents[node1]
    parent_node2 = parents[node2]
    
    l1 = len(parent_node1)
    l2 = len(parent_node2)
    
    if node1 in parent_node2:
        return l2 - parent_node2.index(node1)
        
        
    elif node2 in parent_node1:
        return l1 - parent_node1.index(node2)
        
    # find lowest common root    
    else:
        idx = (l2 if l1 > l2 else l1) - 1
        
        while idx >= 0 and parent_node1[idx].val != parent_node2[idx].val:
            idx -= 1

        return (l1 - idx) + (l2 - idx)