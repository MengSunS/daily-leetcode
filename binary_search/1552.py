class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def check(d):
            cnt = 1
            cur = position[0]
            for j in range(1, n):
                if position[j] - cur >= d:
                    cnt += 1
                    cur = position[j]
            return cnt >= m
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
            
                
                
                
            
        
