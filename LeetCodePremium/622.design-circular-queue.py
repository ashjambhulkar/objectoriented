#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start

class DLinkedList:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class MyCircularQueue:

    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = DLinkedList(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = DLinkedList(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

