class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        s = '#' + s
        p = '#' + p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j] != '*':
                break
            dp[0][j] = True
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == p[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        print(dp)
        return dp[-1][-1]




##### lc 10: Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        s = '#' + s
        p = '#' + p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 2]
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]
                                
