class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
  def helper(self, left, right):
    result = left
    while left and right:
      if right.val < left.val:
        temp = left.next
        test = left.val
        left.val = right.val
        left.next = ListNode(test)
        left.next.next = temp
        right = right.next
      left = left.next
    while result:
      print(result.val)
      result = result.next
       




a = [1,2,4]
b = [1,3,4]
left = ListNode(1)
left.next = ListNode(2)
left.next.next = ListNode(4)

right = ListNode(1)
right.next = ListNode(3)
right.next.next = ListNode(4)

print(Solution().helper(left, right))
