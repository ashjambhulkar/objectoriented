#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        start = prev = Node(None, None, head, None)
        stack = []
        stack.append(head)
        while stack:
            curr = stack.pop()
            curr.prev = prev
            prev.next = curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            curr.child = None    
            prev = curr
        start.next.prev = None
        return start.next

        
# @lc code=end

