class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # (node, status after this node) 去重的是别的路线上比这个早的
        state= 0
        n= len(graph)
        q= deque()
        final_state= (1<<n)- 1
        seen= set()
        
        for i in range(n):
            q.append((i, 1<<i))
            seen.add((i, 1<<i))
        step= 0
        while q:
            for _ in range(len(q)):
                cur, state= q.popleft()
                for j in graph[cur]:
                    new_state= state | (1<< j)
                    if new_state== final_state:
                        return step+ 1
                    if (j, new_state) in seen:
                        continue
                    seen.add((j, new_state))
                    q.append((j, new_state))
            step+= 1
            
        return 0
       
                
            
        
