class Solution:
    def minDays(self, Day: List[int], m: int, k: int) -> int:
        # 除了这个if条件其余一定有解，最坏是最大的day
        if m * k > len(Day): return -1
        l, r = min(Day), max(Day)
        while l < r:
            mid = l+ (r - l)//2
            bouq, flow = 0, 0
            for d in Day:
                flow = 0 if d > mid else flow + 1
                if flow == k:
                    bouq += 1
                    flow = 0
                    if bouq == m: break
                            
            if bouq == m:
                r = mid 
            else:
                l = mid + 1
        return l
                    
                
                
            
        
        
        
