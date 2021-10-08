# word break can be solved by both backtracking + memo, or DP

# backtrackin

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def dfs(pos):
            if pos == len(s):
                return True
            for i in range(pos, len(s)):
                if s[pos: i + 1] in wordDict and dfs(i + 1):
                    return True
            return False
        
        return dfs(0)
        

# DP

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        s = '#' + s
        dp = [False] * (n + 1) 
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j + 1: i + 1] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
