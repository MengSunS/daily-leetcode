# https://www.youtube.com/watch?v=xm5-u_l8tTY
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        events = []
        OPEN, CLOSE = 1, 0
        for x1, y1, x2, y2 in rectangles:
            events.append([y1, x1, x2, OPEN])
            events.append([y2, x1, x2, CLOSE])
        events.sort()
        
        def sweep():
            res = 0
            last_end = 0
            for x1, x2 in active:
                last_end = max(x1, last_end)
                res += max(x2 - last_end, 0)
                last_end = max(last_end, x2)
                
            return res
        
        area, prev_y = 0, events[0][0]
        active = []
        for y, x1, x2, OPEN in events:
            area += (y - prev_y) * sweep()
            if OPEN:
                active.append([x1, x2])
                active.sort()
            else:
                active.remove([x1, x2])
            prev_y = y
        return area % MOD
            
        
