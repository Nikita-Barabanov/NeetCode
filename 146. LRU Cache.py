class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def insert_right(self, node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next, node.prev = node, prev_node
        next_node.prev, node.next = node, next_node

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert_right(Node(key, value))
        self.cache[key] = self.right.prev

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
