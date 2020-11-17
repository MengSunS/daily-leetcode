class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        if not t1 or not t2: return 0
        m, n= len(t1), len(t2)
        
        dp= [[0]*(n+1) for _ in range(2)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if t1[i-1]==t2[j-1]:
                    dp[i%2][j]= dp[(i-1)%2][j-1]+1
                else:
                    dp[i%2][j]= max(dp[(i-1)%2][j], dp[i%2][j-1])
                
        
        return dp[m%2][n]
        
