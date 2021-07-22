class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(x):
            q = collections.deque([x])
            while q:
                cur = q.popleft()
                for nxt, val in enumerate(isConnected[cur]):
                    if val and nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
                        
        def dfs(x):
            for nxt, val in enumerate(isConnected[x]):
                if nxt not in seen and val:
                    seen.add(nxt)
                    dfs(nxt)    
                    
        seen = set()
        n = len(isConnected)
        res = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i) # or bfs(i)
                res += 1
        return res
                




class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.res = n
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        
        if fx != fy:
            self.parent[fx] = fy
            self.res -= 1
    
    def find(self, x):
        i = x
        while self.parent[i] != i:
            i = self.parent[i] 
        # i is the root, now do compress
        while x != i:
            tmp = self.parent[x]
            self.parent[x] = i
            x = tmp
        return i
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        X = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    X.union(i, j)
        return X.res
                
