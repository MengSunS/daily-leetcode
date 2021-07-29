# BFS

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        q = [(root, 0, 0)]
        nq = []
        while q:
            for node, r, c in q:
                d[c].append((r, node.val))
                if node.left:
                    nq.append((node.left, r + 1, c - 1))
                if node.right:
                    nq.append((node.right, r + 1, c + 1))
            q, nq = nq, []
        res = []
        for col in range(min(d), max(d) + 1):
            res.append([val for _, val in sorted(d[col])])
        return res
            

# DFS

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, i, j):
            if not node:
                return 
           
            dfs(node.left, i + 1, j - 1)
            d[j].append((i, node.val))
            dfs(node.right, i + 1, j + 1)
            
        
        d = collections.defaultdict(list)
        dfs(root, 0, 0)
        res = []
        for col in range(min(d), max(d) + 1):
            res.append([val for _, val in sorted(d[col])])
        return res
            
            
