class Node:
    def __init__(self, key=None, val=None, before=None, after=None):
        self.key = key
        self.val = val
        self.before = before
        self.after = after


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.maxi = capacity
        self.head = Node()
        self.tail = Node()
        self.head.after = self.tail
        self.tail.before = self.head


    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.val = value
            self.remove(node)
        else:
            node = Node(key=key, val=value)
        self.insert(node)
        if len(self.cache) > self.maxi:
            self.remove(self.tail.before)
    
    def remove(self, node):
        node.before.after = node.after
        node.after.before = node.before
        node.before, node.after = None, None
        del self.cache[node.key]
    
    def insert(self, node):
        tmp = self.head.after
        self.head.after = node
        node.before = self.head
        node.after = tmp
        tmp.before = node
        self.cache[node.key] = node
    
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
