class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
       
        def dfs(pattern, s, pos_p, pos_s, cache1, cache2):
            if pos_p == len(pattern) and pos_s == len(s):
                return True
            elif pos_p == len(pattern) or pos_s == len(s):
                return False
            
            for i in range(pos_s, len(s)):
                if pattern[pos_p] not in cache1 and s[pos_s:i+1] not in cache2:
                    cache1[pattern[pos_p]] = s[pos_s:i+1]
                    cache2[s[pos_s:i+1]] = pattern[pos_p]
                    if dfs(pattern, s, pos_p + 1, i + 1, cache1, cache2):
                        return True
                    del cache1[pattern[pos_p]]
                    del cache2[s[pos_s:i+1]]
                elif pattern[pos_p] in cache1 and s[pos_s:i+1] in cache2 and cache1[pattern[pos_p]] == s[pos_s:i+1] and cache2[s[pos_s:i+1]] == pattern[pos_p]:
                    if dfs(pattern[pos_p:], s[i+1:], pos_p + 1, i + 1, cache1, cache2):
                        return True
            return False
        
        return dfs(pattern, s, 0, 0, {}, {})
                    
                    
        
