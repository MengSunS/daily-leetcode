class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(startIndex):
            
            if startIndex== len(s):
                return True
            res= []
            for i in range(startIndex, len(s)):
                cand= s[startIndex:i+1]
                if cand in wordDict and dfs(i+1):
                    return True
            
            return False
        
        res= []
        return dfs(0)
            
      


#---

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(startIndex, memo):
            if s[startIndex:] in memo:
                return memo[s[startIndex:]]
            if startIndex== len(s):
                return True
            res= []
            for i in range(startIndex, len(s)):
                cand= s[startIndex:i+1]
                if cand in wordDict and dfs(i+1, memo):
                    memo[s[startIndex:]]= True
                    return True
            memo[s[startIndex:]]= False
            return memo[s[startIndex:]]
        res= []
        memo= {}
        return dfs(0, memo)
              
