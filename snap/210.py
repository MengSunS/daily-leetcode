class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in A:
            graph[a].append(b)
    
        color = {i: 0 for i in range(n)}
        self.possible = True
        res = []
        
        def dfs(node):
            # if not self.possible:
            #     return 
            color[node] = -1
            if node in graph:
                for nxtNode in graph[node]:
                    if color[nxtNode] == -1:
                        self.possible = False
                        return
                    elif color[nxtNode] == 0:
                        dfs(nxtNode)
            color[node] = 1
            res.append(node)
            
        for node in range(n):
            if color[node] == 0 and self.possible:
                dfs(node)
        return res if len(res) == n else []
            
                
        
