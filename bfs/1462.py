class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degree= {i:0 for i in range(n)}
        graph= {i: [] for i in range(n)}
        preset=collections.defaultdict(set)
        
        for p in prerequisites:
            graph[p[0]].append(p[1])
            in_degree[p[1]]+= 1
            preset[p[1]].add(p[0])
            
        start_courses= [c for c in in_degree if in_degree[c]==0]
        q= collections.deque(start_courses)
        while q:
            course= q.popleft()
            for nxt in graph[course]:
                preset[nxt]= preset[nxt] | preset[course]
                in_degree[nxt]-= 1
                if in_degree[nxt]==0:
                    q.append(nxt)
           
        return [True if u in preset[v] else False for u, v in queries]
        
       
        
        
    
       
        
            
        
