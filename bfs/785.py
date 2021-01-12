class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen= {}
        # for i loop是因为可能不是连通图，非连通图每个子图都得是二分图
        for i in range(len(graph)):
            if i in seen:
                continue     
            q= deque([(i, 1)])
            while q:            
                cur, group= q.popleft()               
                for nxt in graph[cur]:
                    #在neighbors for loop里面判断比在上行pop出来判断快，如果neighbor
                    #访问过还放进q等前面都pop出来再判断的话就多了好多额外的前pop后append操作
                    if nxt in seen and seen[nxt]!= -group:
                        return False
                    elif nxt not in seen:
                        seen[nxt]= -group
                        q.append((nxt, -group))        
        return True 

