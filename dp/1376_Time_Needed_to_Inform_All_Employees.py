class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph= collections.defaultdict(list)
        for sub, boss in enumerate(manager):
            graph[boss].append(sub)
        
        q= collections.deque([(headID, 0)])
        res= 0
        #这题找的不是每层最大所有层相加，而是一条最长的时间
        while q:
            boss, cur_time= q.popleft()
            res= max(res, cur_time) #所以这行找个全局最大的数
            
            for sub in graph[boss]:
                q.append([sub, cur_time+ informTime[boss]])
        
        return res
            
            
       
        
