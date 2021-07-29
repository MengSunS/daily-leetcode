class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for x, y, val in zip(equations, values)
            graph[x].append((y, val)
            graph[y].append((x, 1 / val))
       
            
        def dfs(cur, target, val, seen):
            if cur not in graph:
                return False
            if cur == target:
                return True
            for nxt, times in graph[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    val *= times
                    ans = dfs(nxt, target, val, seen)
                    if ans:
                        return ans
                    val /= times
                    seen.remove(nxt)
            return False
        
        res = []
        for s, e in queries:
            res.append(dfs(s, e, 1, set([s])) if dfs(s, e, 1, set([s])) else -1)
        return res
            
                    
                
            
        
