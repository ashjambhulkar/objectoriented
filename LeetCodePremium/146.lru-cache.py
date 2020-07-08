#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class DLinkedList:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None

class LRUCache:

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev =  node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
         

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedList(), DLinkedList()
        self.head.next = self.tail
        self.tail.next = self.head


    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            node = DLinkedList()
            node.val = value
            node.key = key
            self.cache[key] = node
            self._add_node(node)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

