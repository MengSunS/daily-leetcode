class Block:
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None
        
        
    def insert_after(self, new_block):
        tmp = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = tmp
        tmp.before = new_block
    
    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before = None
        self.after = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Block()
        self.tail = Block()
        self.head.after = self.tail
        self.tail.before = self.head
        self.dict = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.dict:
            cur_block = self.dict[key]
            cur_block.keys.remove(key)
        else:
            cur_block = self.head
            
        if cur_block.val + 1!= cur_block.after.val:
            new_block = Block(cur_block.val + 1)
            cur_block.insert_after(new_block)       
        
        cur_block.after.keys.add(key)
            
        self.dict[key] = cur_block.after
        if cur_block.val != 0 and not cur_block.keys:
            cur_block.remove()
         
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
       
        cur_block = self.dict[key]
        del self.dict[key]
        cur_block.keys.remove(key)
        
        if cur_block.val - 1 != cur_block.before.val:
            new_block = Block(cur_block.val - 1)
            cur_block.before.insert_after(new_block)
            
        cur_block.before.keys.add(key)
        self.dict[key] = cur_block.before
            
        if cur_block.val != 0 and not cur_block.keys:
            cur_block.remove()        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.tail.before.val == 0:
            return ""
        ans = self.tail.before.keys.pop()
        self.tail.before.keys.add(ans)
        return ans
           

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.head.after.val == 0:
            return ""
        ans = self.head.after.keys.pop()
        self.head.after.keys.add(ans)
        return ans
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
