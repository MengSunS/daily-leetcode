class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        graph= collections.defaultdict(list)
        for i in range(len(pid)):
            graph[ppid[i]].append(pid[i])
        
        q= collections.deque([kill])
        res= []
        while q:
            cur= q.popleft()
            res.append(cur)
            for sub in graph[cur]:
                q.append(sub)
        return res
            
            
        
