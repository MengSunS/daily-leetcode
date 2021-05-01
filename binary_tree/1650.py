# Method 1: same to lc 160. 不同点是这道题if p1也可以if p1.parent也可以，p1时是走最上面的根节点再往上的那个None,也可以不走，不影响长度相等的条件。而160那道题必须走最后一个点的下一个None,因为有可能不相交，而这道题LCA一定有答案。

 Reason why it works: count the number of nodes traveled from head1-> tail1 -> head2 -> intersection point and head2 -> tail2-> head1 -> intersection point.
https://stackoverflow.com/questions/1594061/check-if-two-linked-lists-merge-if-so-where

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2= p, q
        while p1!= p2:
            p1= p1.parent if p1 else q
            p2= p2.parent if p2 else p
        return p1


#Method 2:

class Solution2:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        while q:
            if q in seen:
                return q
            q = q.parent

# Method 3: recursion

class Solution3:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        def traverse_up(node):
            if not node or node in seen:
                return node
            seen.add(node)
            return traverse_up(node.parent)
        
        return traverse_up(p) or traverse_up(q)        
