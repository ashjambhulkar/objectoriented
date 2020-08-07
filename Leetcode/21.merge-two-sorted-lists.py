#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if None in (l1, l2):
        #     return l1 or l2

        # dummy = cur = ListNode(0)
        # dummy.next = l1
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         l1 = l1.next
        #     else:
        #         nxt = cur.next
        #         cur.next = l2
        #         tmp = l2.next
        #         l2.next = nxt
        #         l2 = tmp
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next

        if None in (l1, l2):
            return l1 or l2
        
        root = cur = ListNode(0)
        cur.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                temp = cur.next
                cur.next = l2
                test = l2.next
                l2.next = temp
                l2 = test
            cur = cur.next
        cur.next = l1 or l2
        return root.next
            

# @lc code=end

