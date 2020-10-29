------method1 dfs+memo top down---

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        memo= {}
        return self.dfs(1, n, memo)
    
    def dfs(self, a, b, memo):
        if (a, b) in memo:
            return memo[(a, b)]
        if a>= b:
            return 0
        
        min_value= sys.maxsize
        for i in range(a, b+1):
            min_value= min(min_value, max(self.dfs(a, i-1, memo)+ i, self.dfs(i+1, b, memo)+ i))
        
        memo[(a, b)]= min_value
        
        return memo[(a, b)]



-------method2: dp bottom up---

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp= [[sys.maxsize]*(n+1) for _ in range(n+1)]
        
        for j in range(n+1):
            for i in range(j, 0, -1):
                if i==j:
                    dp[i][j]= 0
                elif i+1==j:
                    dp[i][j]= i
                else:
                    for x in range(i+1, j):
                        dp[i][j]= min(dp[i][j], max(dp[i][x-1]+x, dp[x+1][j]+x))
        
        return dp[1][n]
        
