# course schedule系列，有向图，拓扑排序；此题如果每次查connect会超时，索性剥洋葱向下传递时把每个点的preSet joint一下
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        preSet = defaultdict(set)
        inDegree = {i: 0 for i in range(n)}
        for x, y in prerequisites:
            graph[x].append(y)
            preSet[y].add(x)
            inDegree[y] += 1
        
        bfs = deque([i for i in range(n) if not inDegree[i]])
        while bfs:
            cur = bfs.popleft()
            for nxt in graph[cur]:
                preSet[nxt] |= preSet[cur]
                inDegree[nxt] -= 1
                if not inDegree[nxt]:
                    bfs.append(nxt)
        
        return [u in preSet[v] for u, v in queries]
            
        
        
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
        
       
        
        
    
       
        
            
        
