# Method 1: heapq, push end

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hq = []
        for start, end in intervals:
            if hq and start>= hq[0]:
                heapq.heappop(hq)
            heapq.heappush(hq, end)
        return len(hq)
                
                

# Method 2: sweeping line, start & end two arrays sorted

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_lst= sorted([interval[0] for interval in intervals])
        end_lst= sorted([interval[1] for interval in intervals])
        p1, p2= 0, 0
        cnt= 0
        while p1< len(start_lst):
            if start_lst[p1]>= end_lst[p2]:
                p2+= 1
            else:
                cnt+= 1
            p1+= 1
            
        return cnt
                

