import random

class Node:
    
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down
        
class Skiplist:

    def __init__(self):
        self.head = Node()
        

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            node = node.down
        return False
        

    def add(self, num: int) -> None:
        prev = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            prev.append(node)
            node = node.down
            
        down = None
        insert = True
        while insert and prev:
            node = prev.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = random.choice([0, 1])
        
        if insert:
            self.head = Node(-1, None, self.head)
                  

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                node.right = node.right.right
                found = True
            node = node.down
        return found
                
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
