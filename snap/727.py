# two strings, pattern match problem, order matters, so NOT hashmap + sliding widow, DP problem. 
# dp[i][j], if include ith ele in s, whats the minmum window size can make first jth ele in t. if not able to, inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        s = '#' + s
        t = '#' + t
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == t[j]:
                    if j == 1:
                        dp[i][j] = 1 # important, reset the start
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j] + 1
        f = [dp[i][n] for i in range(m + 1)]
        mini = min(f)
        if mini == float('inf'):
            return ''
        for i in range(len(f)):
            if f[i] == mini:
                return s[i- mini + 1: i + 1]
        
        
