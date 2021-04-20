class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

        
class DLinkList:
    def __init__(self):
        self.anchor = Node(None, None)
        self.anchor.next = self.anchor.prev = self.anchor
        self.size = 0
    
     
    def append(self, node):
        node.next = self.anchor.next
        node.prev = self.anchor
        node.next.prev = node
        self.anchor.next = node
        self.size += 1
        
        
    def pop(self, node=None):
        if not node:
            node = self.anchor.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1
        return node
    
      
class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = collections.defaultdict(DLinkList)
        self.minf = 0
        self.amount = 0
        self.maxi = capacity
          
    def update(self, node):
        
        self.freq[node.freq].pop(node)
        if self.minf == node.freq and self.freq[node.freq].size == 0:
            self.minf += 1
        node.freq += 1
        self.freq[node.freq].append(node)

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val
            

    def put(self, key: int, value: int) -> None:
        if self.maxi == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            node.val = value
        else:
            if self.amount == self.maxi:
                del_node = self.freq[self.minf].pop()
                del self.cache[del_node.key]
                self.amount -= 1
            node = Node(key, value)
            self.cache[key] = node
            self.minf = 1
            self.freq[1].append(node)
            self.amount += 1
            
            
            
        
        
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
