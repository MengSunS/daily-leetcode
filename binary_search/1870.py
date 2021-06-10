class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        l, r = 1, math.ceil(max(dist) / (hour - (n - 1)))
        if n - 1 >= hour:
            return -1
        while l < r:
            mid = l + (r - l) // 2
            time = dist[-1] / mid + sum(math.ceil(d / mid) for d in dist[:-1])
            if time > hour:
                l = mid + 1
            else:
                r = mid 
                
        return l
    
    
        
        
