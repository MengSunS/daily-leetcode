class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            res.append([node.val for node in q])
            stack = []
            # for node in [q.popleft() for _ in range(len(q))]:
            for node in q:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            q = stack
                    
        return res
