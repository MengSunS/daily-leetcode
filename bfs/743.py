class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph= defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))    
        hp= [(0, K)]
        arrivals= {}
        print(graph)
        while hp:
            acc_t, node= heapq.heappop(hp)
            # print('time:', acc_t, 'node:',node)
            #这个if 必须放在外面，因为for loop里面的if只是判断是否已经尘埃落定，
            #如果比它更快的还在heap中排队中的话，比它慢的也会入heap,那么快的会先一步
            #尘埃落定进arrivals没错，但后面的while会让慢的把快的覆盖掉
            if node in arrivals: continue
            arrivals[node]= acc_t    
            for nxt, delta_t in graph[node]:
                # print('nxt:', nxt, 'delta_t:', delta_t)
                if nxt in arrivals: continue
                heapq.heappush(hp, (acc_t+ delta_t, nxt))
                # print('heap:', hp)
            # print('-----')
        
        return max(arrivals.values()) if len(arrivals)==N else -1
    
    
# Method 2: normal q bfs, allow seen nodes go into again, if value is smaller, replace

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph= defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))    
        q= deque([(K, 0)])
        arrivals= {}
        while q:
            node, acc_t= q.popleft()
            if node not in arrivals or arrivals[node]> acc_t:
                arrivals[node]= acc_t
                for nxt, delta_t in graph[node]:
                    q.append((nxt, delta_t+ acc_t))
        return max(arrivals.values()) if len(arrivals)==N else -1

    
    
       
       
       
              
       
       
       
