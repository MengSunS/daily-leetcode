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
        
            
            
        
