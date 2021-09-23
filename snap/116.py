class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = collections.deque([root])
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                node.next = q[0] if i != size - 1 else None
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
        return root
        
