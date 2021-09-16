class Solution:
    def minDistance(self, s: str, t: str) -> int:
        if not s: return len(t)
        if not t: return len(s)
        m, n = len(s), len(t)
        s = '#' + s
        t = '#' + t
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                dp[i][0] = i
                dp[0][j] = j
      
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == t[j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
                
        
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        s = '#' + s
        t = '#' + t
        def dfs(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0:
                return j
            if j == 0:
                return i
            
            memo[(i, j)] = float('inf')
            if s[i] == t[j]:
                memo[(i, j)] = min(memo[(i, j)], dfs(i - 1, j - 1, memo))
            else:
                memo[(i, j)] = min(memo[(i, j)], min(dfs(i - 1, j - 1, memo), dfs(i, j - 1, memo), dfs(i - 1, j, memo)) + 1)
            return memo[(i, j)]
        
        return dfs(len(s) - 1, len(t) - 1, {})
                
                    
