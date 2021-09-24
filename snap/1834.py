class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        res = []
        now = tasks[0][0]
        h = []
        while len(res) < len(tasks):
            while i < len(tasks) and now >= tasks[i][0]:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                t_diff, index = heapq.heappop(h)
                now += t_diff
                res.append(index)
            elif i < len(tasks):
                now = tasks[i][0]
        return res
            
                
            
        
        
