class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N= len(A)
        M= 1<<N
        dp= [[sys.maxsize//2]*N for _ in range(M)]
        parent= [[-1]*N for _ in range(M)]
        
        dist= [[0]*N for _ in range(N)]
        

        def cal_dist(i, j):
            a, b= A[i], A[j]
            min_len= min(len(a), len(b))
            for i in range(min_len, 0, -1):
                if a[-i:]== b[:i]:
                    return len(b[i:])
            return len(b)
        
            
        def combine(a, b):
            min_len= min(len(a), len(b))
            for i in range(min_len, 0, -1):
                if a[-i:]== b[:i]:
                    return a+b[i:]
            return a+b
        
        
        for i in range(N):
            for j in range(N):
                if i!= j:
                    dist[i][j]= cal_dist(i, j)
       
        
        for i in range(N):     
                dp[1<<i][i]= len(A[i])

        
        for status in range(M):
            for last in range(N):
                if (status & (1<<last))==0: continue
                pre_status= status- (1<<last)
                for pre_last in range(N):
                    if (pre_status&(1<<pre_last))==0: continue
                    if dp[status][last]> dp[pre_status][pre_last]+ dist[pre_last][last]:
                        dp[status][last]= dp[pre_status][pre_last]+ dist[pre_last][last]
                        parent[status][last]= pre_last
        
                        
        
        start = min(enumerate(dp[M - 1]), key=lambda x: x[1])[0]
        last= start
        path= collections.deque([last])
        status= M-1
        
        while parent[status][last]!= -1:
            pre_last= parent[status][last]
            path.appendleft(pre_last)
            status= status- (1<<last)
            last= pre_last
        
        
        ans= A[path[0]]
        for i in range(1, len(path)):
            ans= combine(ans, A[path[i]])
        return ans
        
       
    
            
    
    
            
            
                    
                
            
        
