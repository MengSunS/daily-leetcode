class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, in_degree= self.build_graph(numCourses, prerequisites)
        
        start_courses= [course for course in graph if in_degree[course]==0]
        q= collections.deque(start_courses)
        res= []
        while q:
            course= q.popleft()
            res.append(course)
            for nxt in graph[course]:
                in_degree[nxt]-= 1
                if in_degree[nxt]== 0:
                    q.append(nxt)
        
        return res if len(res)== len(graph) else []
    
    def build_graph(self, n, ps):
        in_degree, graph= {i:0 for i in range(n)}, {i:[] for i in range(n)}
        for p in ps:
            in_degree[p[0]]+= 1
            graph[p[1]].append(p[0])
        return graph, in_degree
        
        
