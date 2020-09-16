## Three facts to know about BST

> Inorder traversal of BST is an array sorted in the ascending order.

To compute inorder traversal follow the direction Left -> Node -> Right.

```
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
```
![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/450_inorder.png)

> Successor = "after node", i.e. the next node, or the smallest node after the current one.

It's also the next node in the inorder traversal. To find a successor, go to the right once and then as many times to the left as you could.

```
def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root
```

> Predecessor = "before node", i.e. the previous node, or the largest node before the current one.

It's also the previous node in the inorder traversal. To find a predecessor, go to the left once and then as many times to the right as you could.

```
def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root
```

![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/succ2.png)

## Approach 1: Recursion
Intuition

There are three possible situations here :

1.  Node is a leaf, and one could delete it straightforward : node = null.
      ![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/del_leaf.png)
2. Node is not a leaf and has a right child. Then the node could be replaced by its successor which is somewhere lower in the right subtree. Then one could proceed down recursively to delete the successor.
   ![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/del_succ.png)
3. Node is not a leaf, has no right child and has a left child. That means that its successor is somewhere upper in the tree but we don't want to go back. Let's use the predecessor here which is somewhere lower in the left subtree. The node could be replaced by its predecessor and then one could proceed down recursively to delete the predecessor.
  ![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/del_pred.png)
   
### Algorithm

1.  If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).

2.  If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).

3.  If key == root.val then the node to delete is right here. Let's do it :

    1.  If the node is a leaf, the delete process is straightforward : root = null.

    2.  If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).

    3.  If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).

4.  Return root.


### Implementation
![](https://leetcode.com/problems/delete-node-in-a-bst/Figures/450/implem2.png)

```
class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
```
### Complexity Analysis

> Time complexity : O(logN). During the algorithm execution we go down the tree all the time - on the left or on the right, first to search the node to delete O(H1)time complexity as already discussed) and then to actually delete it. H1 is a tree height from the root to the node to delete. Delete process takes O(H2) time, where H2
is a tree height from the root to delete to the leafs. That in total results in O(H1+H2
​)=O(H) time complexity, where H is a tree height, equal to logN in the case of the balanced tree.

> Space complexity : O(H) to keep the recursion stack, where H is a tree height. H =logN for the balanced tree.