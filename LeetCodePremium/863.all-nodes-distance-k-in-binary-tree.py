#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            node, depth = queue.popleft()
            if depth == K:
                return [node.val]+[x.val for x, y in queue]
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, depth+1))
        return []
        

# @lc code=end

