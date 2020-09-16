#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        string = ""
        def rserialize(root):
          nonlocal string
          if not root:
            string += "#,"
            return
          string += str(root.val)+","
          rserialize(root.left)
          rserialize(root.right)
        rserialize(root)
        return string
        

    def deserialize(self, data: str) -> TreeNode:
        def rdeserialize(raw):
          if raw[0] == "#":
            raw.pop(0)
            return
          root = TreeNode(raw[0])
          raw.pop(0)
          root.left = rdeserialize(raw)
          root.right = rdeserialize(raw)
          return root
        raw = data.split(",")
        return rdeserialize(raw)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

