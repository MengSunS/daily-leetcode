class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 4 + 1
        self.arr = [Bucket() for i in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self._hash(key)
        self.arr[bucket].update(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self._hash(key)
        return self.arr[bucket].get(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self._hash(key)
        self.arr[bucket].remove(key)

class Node:
    def __init__(self, val, nextVal=None):
        self.val = val
        self.next = nextVal

class Bucket:
    def __init__(self):
        self.dummy = Node((-1, -1))
        
    def update(self, key, val):
        cur = self.dummy
        found = False
        while cur:
            if cur.val[0] == key:
                cur.val = (key, val)
                found = True
                break
            cur = cur.next
        if not found:
            newNode = Node((key, val))
            newNode.next = self.dummy.next
            self.dummy.next = newNode
    
    def get(self, key):
        cur = self.dummy
        found = False
        while cur:
            if cur.val[0] == key:
                found = True
                return cur.val[1]
            cur = cur.next
        return -1
    
    def remove(self, key):
        prev, cur = self.dummy, self.dummy.next
        while cur and cur.val[0] != key:
            prev, cur = prev.next, cur.next
        if cur:
            prev.next = cur.next
           
        
    
        
                
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
