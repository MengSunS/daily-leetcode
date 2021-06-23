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

        
