class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq= collections.deque([])
        res= -sys.maxsize
        for j in range(len(points)):
            while dq and points[j][0]- points[dq[0]][0]> k:
                dq.popleft()
            if dq:
                res= max(res, points[j][0]+ points[j][1]+ points[dq[0]][1]- points[dq[0]][0])
            t= points[j][1]- points[j][0]
            while dq and t> points[dq[-1]][1]- points[dq[-1]][0]:
                dq.pop()
            dq.append(j)
        return res
        
        
        
        
        
        
#         max(yi+ yj- xi+ xj)        
#         max(yi- xi)+ xj+ yj for xj-xi<= k scan over xj O(n)
        
#         XX[XX] j X
        
        
