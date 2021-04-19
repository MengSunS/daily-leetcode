# hashmap: {key: node}
# doubleLinkedList: <->node<->
# node.val, node.key, node.before, node.after
# two dummy nodes: self.head, self.tail
class DLinkNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.before = None
        self.after = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.maxi = capacity
        self.size = 0
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.after = self.tail
        self.tail.before = self.head
        self.dict = {} # {key: node}
        

    def get(self, key: int) -> int:
        node = self.dict.get(key, None)
        if not node:
            return -1
        self.remove(node)
        self.insert(node)
        # self.dict[key] = node
        return node.val
            

    def put(self, key: int, value: int) -> None: #update
        node = self.dict.get(key, None)
        if not node:
            node = DLinkNode()
            self.size += 1
        else:
            self.remove(node)
        self.dict[key] = node
        node.key = key
        node.val = value
        self.insert(node)
        if self.size > self.maxi:
            node = self.pop_tail()
            del self.dict[node.key]
            self.size -= 1
            
           
    
    def remove(self, node):
        node.before.after = node.after
        node.after.before = node.before
        node.before = None
        node.after = None


    
    def insert(self, node):
        tmp = self.head.after
        self.head.after = node
        node.before = self.head
        node.after = tmp
        tmp.before = node
           
    
    def pop_tail(self):
        node = self.tail.before
        self.remove(node)
        return node
        
        
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
