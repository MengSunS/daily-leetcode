class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append([l, -h, r])
            events.append([r, 0, 0])
        events.sort()
        
        res = [[0, 0]] # pos, height
        active = [(0, inf)]
        for pos, negH, r in events:
            while active[0][1] <= pos:
                heapq.heappop(active)
            if negH:
                heapq.heappush(active, (negH, r))
            if res[-1][1] != -active[0][0]:
                res.append([pos, -active[0][0]])
        return res[1:]
        
