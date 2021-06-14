#---Method1: for loop Dp---

class Solution:
    def minInsertions(self, s: str) -> int:
        n= len(s)
        dp= [[0]*n for _ in range(n)]
        
       
        #i, j 不对，不知道为什么
        for d in range(1, n):
            for i in range(n-d):
                j= i+ d                  
                if s[i]==s[j]:
                    dp[i][j]= dp[i+1][j-1]
                else:
                    dp[i][j]= min(dp[i][j-1], dp[i+1][j])+1
        
        return dp[0][n-1]

#------Method 2: recursion DP--

class Solution:
    def minInsertions(self, s: str) -> int:
        n= len(s)
        @functools.lru_cache(None)
        def dp(i, j):
            if i>=j:
                return 0
            if s[i]==s[j]:
                return dp(i+1, j-1)
            else:
                return min(dp(i+1, j), dp(i, j-1))+1
        
        return dp(0, n-1)
