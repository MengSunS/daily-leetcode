class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        tmp = 0
        times = []
        for s, e in intervals:
            times.append((s, 1))
            times.append((e, -1))
        times.sort()
        for _, flag in times:
            tmp += flag
            res = max(res, tmp)
        return res
        
            
            
# heapq, 放结束时间

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = []
        intervals.sort(key=lambda x: x[0])
        for s, e in intervals:
            if pq and pq[0] <= s:
                heapq.heapreplace(pq, e)
            else:
                heapq.heappush(pq, e)
        return len(pq)
                
