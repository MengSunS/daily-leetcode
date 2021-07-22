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
                
            
