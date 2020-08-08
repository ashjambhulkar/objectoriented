#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def rsearialize(root, string):
            if not root:
                string += '#,'
            else:
                string += str(root.val) + ','
                string = rsearialize(root.left, string)
                string = rsearialize(root.right, string)
            return string
        return rsearialize(root, '')
        


    def deserialize(self, data):
        def ldeserialize(word):
            if word[0] == '#':
                word.pop(0)
                return None
            root = TreeNode(word[0])
            word.pop(0)
            root.left = ldeserialize(word)
            root.right = ldeserialize(word)
            return root
            

        result = data.split(",")
        root = ldeserialize(result)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

