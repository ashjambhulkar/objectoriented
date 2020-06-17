# count = 0
# def depth(root):
#   if not root:
#     return 0
#   left = depth(root.left)
#   right = depth(root.right)
#   count = max(count, left+right+1)
#   return max(left, right) + 1
# depth(root)
# return count - 1

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next  

class Solutions:
  def helper(self, head):
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
    return slow