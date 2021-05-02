# time O(N), N is number of all nodes; space O(D), D is diameter
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
        
