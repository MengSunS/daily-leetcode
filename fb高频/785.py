class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        seen = {}
        for i in range(n - 1):
            if i not in seen:
                seen[i] = 1 # absent when bfs
                if not self.dfs(i, 1, seen, graph): # or self.bfs(i, 1, seen, graph)
                    return False
        return True
    
    def dfs(self, node, color, seen, graph):
        for nxt in graph[node]:
            if nxt not in seen:
                seen[nxt] = -color
                if not self.dfs(nxt, -color, seen, graph):
                    return False
            elif seen[nxt] == color:
                return False
        return True
    
    def bfs(self, node, color, seen, graph):
        q = collections.deque([(node, color)])
        while q:
            node, color = q.popleft()
            for nxt in graph[node]:
                if nxt not in seen:
                    seen[nxt] = -color
                    q.append((nxt, -color))
                elif seen[nxt] == color:
                    return False
        return True
                
            
        
