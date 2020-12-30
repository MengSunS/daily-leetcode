# https://www.youtube.com/watch?v=Tf9v-fNijac

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n= len(arr)
        if n== m: return n
        
        arr= [0]+ arr
        day= [0]*len(arr)
        
        for i in range(1, len(arr)):
            day[arr[i]]= i
            
        q= collections.deque([])
        res= -1
        for i in range(1, n+1):
            if q and q[0][1]== i-m:
                q.popleft()
            while q and day[i]> q[-1][0]:
                q.pop()
            q.append((day[i], i))
            if i< m: 
                continue 
            
            left, right= sys.maxsize, sys.maxsize
            if i-m>=1: left= day[i-m]
            if i+1< len(day): right= day[i+1]
            if q[0][0]< left and q[0][0]< right:
                res=max(res, min(left, right)-1)
        return res 
            
        
