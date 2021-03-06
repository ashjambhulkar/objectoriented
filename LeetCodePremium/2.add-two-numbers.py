#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        # carry = 0
        # root = n = ListNode(0)
        # while l1 or l2 or carry:
        #     left = right = 0
        #     if l1:
        #         left = l1.val
        #         l1 = l1.next
        #     if l2:
        #         right = l2.val
        #         l2 = l2.next
        #     carry, val = divmod(left+right+carry, 10)
        #     n.next = ListNode(val)
        #     n = n.next
        # return root.next

        carry = 0
        start = prev = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            prev.next = ListNode(val)
            prev = prev.next
        return start.next


# @lc code=end

