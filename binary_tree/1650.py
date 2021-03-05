# Method 1: same to lc 160. Reason why it works: https://stackoverflow.com/questions/1594061/check-if-two-linked-lists-merge-if-so-where

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2= p, q
        while p1!= p2:
            p1= p1.parent if p1 else q
            p2= p2.parent if p2 else p
        return p1


#Method 2:

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited= set()
        visited.add(p)
        while p.parent:
            p= p.parent
            visited.add(p)
        if q in visited:
            return q
        while q.parent:
            if q.parent in visited:
                return q.parent
            q= q.parent
        
