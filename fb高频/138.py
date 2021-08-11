"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# two pass, 但简单明了 O(2N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        clone_map = {}
        node = head
        while node:
            clone_map[node] = Node(node.val)
            node = node.next
        
        for node in clone_map.keys():
            if node.next:
                clone_map[node].next = clone_map[node.next]
            if node.random:
                clone_map[node].random = clone_map[node.random]
            
        return clone_map[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        dic, prev = {}, None
        while head:
            if head not in dic:
                dic[head] = Node(head.val, None, None)
            if prev:
                prev.next = dic[head]
            else:
                nhead = dic[head]
            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val, None, None)
                dic[head].random = dic[head.random]
            prev, head = dic[head], head.next
            
        return nhead

        
