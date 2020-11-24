class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color= [0]* len(graph)
        
        for i in range(len(graph)):
            if color[i]!=0:
                continue
            color[i]= 1
            
            q= deque()
            q.append(i)
            while q:
                node= q.popleft()
                for neighbor in graph[node]:
                    if color[neighbor]== 0:
                        color[neighbor]= -color[node]
                        q.append(neighbor)
                    else:
                        if color[neighbor]== color[node]:
                            return False
        return True
        
        

