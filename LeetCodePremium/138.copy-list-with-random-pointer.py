#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pass

            

# @lc code=end

