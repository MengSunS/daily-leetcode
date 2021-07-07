class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 4 + 1
        self.arr = [Bucket() for i in range(self.size)]
        
    def _hash(self, key):
        return key % self.size
    
    def add(self, key: int) -> None:
        bucket = self._hash(key)
        if not self.arr[bucket].exist(key):
            self.arr[bucket].add(key)
            
    def remove(self, key: int) -> None:
        bucket = self._hash(key)
        if self.arr[bucket].exist(key):
            self.arr[bucket].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self._hash(key)
        return self.arr[bucket].exist(key)
        
class Node:
    def __init__(self, val, nextVal=None):
        self.val = val
        self.next = nextVal

class Bucket:
    def __init__(self):
        self.dummy = Node(-1)
    
    def add(self, key):
        newNode = Node(key)
        newNode.next = self.dummy.next
        self.dummy.next = newNode
    
    def remove(self, key):
        prev, cur = self.dummy, self.dummy.next
        while cur and cur.val != key:
            prev, cur = prev.next, cur.next
        prev.next = cur.next
    
    def exist(self, key):
        cur = self.dummy.next
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False
        
        
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
