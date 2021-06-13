# lee215

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -float('inf')
        deque = collections.deque()
        for x, y in points:
            while deque and deque[0][1] + k < x:
                deque.popleft()
            if deque:
                res = max(res, x + y + deque[0][0])
            while deque and deque[-1][0] <= y - x:
                deque.pop()
            deque.append([y - x, x])
        return res
        
# lee215 prority queue 

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        pq = []
        res = -float('inf')
        for x, y in points:
            while pq and pq[0][1] + k < x:
                heapq.heappop(pq)
            if pq:
                res = max(res, -pq[0][0] + x + y)
            heapq.heappush(pq, [x - y, x])
        return res        
        
        
       
        
# max(yi - xi) + (xj + yj)  loop j 
# for one j:    xj - xi <= k
    
        
        





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
        
        
