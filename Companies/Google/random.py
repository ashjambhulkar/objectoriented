class LinkedList:
    def __init__(self, key, value):
        self.node = (key, value)
        self.next = None


class Solution:
    def __init__(self):
        self.size = 1000
        self.h = [None] * self.size

    def get(self, key):
        curr = self.h[key%self.size]
        while curr:
            if curr.node[0] == key:
                return curr.node[1]
            curr = curr.next
        return -1

    def update(self, key, value):
        hash_key = key % self.size
        if not self.h[hash_key]:
            self.h[hash_key] = LinkedList(key, value)
        else:
            curr = self.h[hash_key]
            while curr.next:
                if curr.node[0] == key:
                    curr.node[1] = value
                else:
                    curr.next

            if curr.node[0] == key:
                curr.node[1] = value
            else:
                curr.next = LinkedList(key, value)

    def delete(self, key):
        index = key % self.size
        cur = prev = self.h[index]
        if not cur:
            return
        if cur.node[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.node[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


