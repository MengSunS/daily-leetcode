----Method 1: bottom up-----


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s: return 0
        
        n= len(s)
        dp= [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i][j]= 1
                if i+1== j:
                    if s[i]== s[j]:
                        dp[i][j]= 1
                    else:
                        dp[i][j]=2
         
        for d in range(1, n):
            for left in range(0, n-d):
                right= left+ d
                dp[left][right]= dp[left][right-1]+ 1 #worst case
                for k in range(left, right):
                    if s[right]== s[k]:
                        dp[left][right]= min(dp[left][right], dp[left][k]+ dp[k+1][right-1])
                        
        return dp[0][n-1]
               
------ Method 2: top down---- 

class Solution:
    def strangePrinter(self, s: str) -> int:
        n= len(s)
        dp= [[0]*n for _ in range(n)]
        return self.dfs(0, n-1, dp, s)
        
    def dfs(self, i, j, dp, s):
        if i> j: return 0
        if dp[i][j]>0: return dp[i][j]
        
        min_ij= self.dfs(i, j-1, dp, s)+ 1
        
        for k in range(i, j):
            if s[k]== s[j]:
                min_ij= min(min_ij, self.dfs(i, k, dp, s)+ self.dfs(k+1, j-1, dp, s))
        dp[i][j]= min_ij
        return dp[i][j]
        
