#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        result = lists[0]
        for i in range(1, len(lists)):
            l1 = result
            l2 = lists[i]
            dummy = curr = ListNode(0)
            curr.next = l1
            while l1 and l2:
                if l1.val <= l2.val:
                    l1 = l1.next
                else:
                    nxt = curr.next
                    curr.next = l2
                    temp = l2.next
                    l2.next = nxt
                    l2 = temp
                curr = curr.next
            curr.next = l1 or l2
            result = dummy.next
        return result
       
# @lc code=end

