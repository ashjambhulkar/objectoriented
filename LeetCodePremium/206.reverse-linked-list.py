#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative soltution
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        while head:
            test = head.next
            head.next = temp
            temp = head
            head = test
        return temp

    # recursive solution
    # def reverseList(self, head: ListNode) -> ListNode:
    #   if not head or not head.next:
    #     return head
    #   node = self.reverseList(head.next)
    #   head.next.next = head
    #   head.next = None
    #   return node
    

        
# @lc code=end

