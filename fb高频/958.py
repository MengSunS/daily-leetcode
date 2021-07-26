# time is O(n) for dfs and bfs, space is O(h) for dfs and O(n) for bfs
class Solution:
    def isCompleteTree_dfs(self, root: TreeNode) -> bool:
        self.total = 0
        self.max_pos = 0
        def dfs(node, pos):
            if not node:
                return 
            self.total += 1
            self.max_pos = max(self.max_pos, pos)
            dfs(node.left, 2 * pos)
            dfs(node.right, 2 * pos + 1)
            
        dfs(root, 1)
        return self.total == self.max_pos
    
    def isCompleteTree_bfs(self, root: TreeNode) -> bool:
        q = [(root, 1)]
        nq = []
        res = [1]
        while q:
            for node, pos in q:
                if node.left:
                    res.append(2 * pos)
                    nq.append((node.left, 2 * pos))
                if node.right:
                    res.append(2 * pos + 1)
                    nq.append((node.right, 2 * pos + 1))
            q, nq = nq, []
        return len(res) == res[-1]
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = [root]
        i = 0
        while q[i]:
            q.append(q[i].left)
            q.append(q[i].right)
            i += 1
        return not any(q[i:])
