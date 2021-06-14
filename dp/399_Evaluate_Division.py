class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph= self.build_graph(equations, values)
        
        res= []
        for x, y in queries:
            if y not in graph:
                res.append(-1)
                continue
            visited= set()
            visited.add(x)
            res.append(self.dfs(x, y, graph, 1, visited, {}))
        
        return res
    
    def dfs(self, cur, target, graph, times, visited, memo):
        if (cur, target) in memo:
            return memo[(cur, target)]
        
        if cur== target:
            return times
        
        ans= -1
        for neigh, t in graph[cur]:
            if neigh in visited:
                continue
            visited.add(neigh)
            ans= self.dfs(neigh, target, graph, times*t, visited, memo)
            if ans!= -1:
                break        
            visited.remove(neigh)
            
        
        memo[(cur, target)]= ans
        return memo[(cur, target)]
        
        
    
    def build_graph(self, equations, values):
        graph= collections.defaultdict(list)
        
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        return graph
            
        
        
            
            
            
        
            
        
