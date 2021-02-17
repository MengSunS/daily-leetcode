# - write memo


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dfs(startIndex, memo):
            if startIndex== len(s):
                return [[]]
            if s[startIndex:] in memo:
                return memo[s[startIndex:]]
            
            res= []
            for i in range(startIndex, len(s)):
                cand= s[startIndex:i+1]
                if cand in wordDict:
                    for nxt_lst in dfs(i+1, memo):
                        res.append([cand]+ nxt_lst)
            memo[s[startIndex:]]= res
            return res
    
        wordDict= set(wordDict)
        return [' '.join(word) for word in dfs(0, {})]
        
        
- use @lru_cache(None)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(startIndex):
            if startIndex== len(s):
                return [[]]
            res= []
            for i in range(startIndex, len(s)):
                cand= s[startIndex:i+1]
                if cand in wordDict:
                    for nxt_lst in dfs(i+1):
                        res.append([cand]+ nxt_lst)
            return res
    
        wordDict= set(wordDict)
        return [' '.join(word) for word in dfs(0)]
        
