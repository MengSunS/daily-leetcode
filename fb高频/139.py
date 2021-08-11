class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]
        
        # dp[i]: the first i elements whether breakable. s[:i]
        # dp[j] = dp[i] and s[i:j] in wordset, for i in range(j)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        @lru_cache(None)
        def breakable(pos):
            if pos == len(s):
                return True
            
            for i in range(pos, len(s)):
                if s[pos:i + 1] in wordSet and breakable(i + 1):
                    return True
                
           
            return False

        return breakable(0)        
