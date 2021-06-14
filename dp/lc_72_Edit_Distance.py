#-------Method 1: dfs+ memo, @functools.lru_cache(None)---
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @functools.lru_cache(None)
        def dfs(w1, w2):
            
            if not w1 and not w2: return 0
            elif not w2: return len(w1)
            elif not w1: return len(w2)    
            else:
                             
                if w1[-1]==w2[-1]: 
                    return dfs(w1[:-1], w2[:-1])
                else:
                    return min(dfs(w1, w2[:-1]), dfs(w1[:-1], w2), dfs(w1[:-1], w2[:-1]))+ 1
        
        return dfs(word1, word2)
        
--------dfs + memo 常规写法-------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dfs(word1, word2, {})
    
    def dfs(self, w1, w2, memo):
        if (w1, w2) in memo:
            return memo[(w1, w2)]
        
        if not w1 and not w2:
            return 0
        elif not w1: 
            memo[(w1, w2)]= len(w2)
            return memo[(w1, w2)]
        elif not w2:
            memo[(w1, w2)]= len(w1)
            return memo[(w1, w2)]
       
        elif w1 and w2:
            
            if w1[-1]== w2[-1]:
                memo[(w1, w2)]= self.dfs(w1[:-1], w2[:-1], memo)

            else:
                memo[(w1, w2)]= min(self.dfs(w1, w2[:-1], memo), self.dfs(w1[:-1], w2, memo), self.dfs(w1[:-1], w2[:-1], memo))+1
        
        return memo[(w1, w2)]

-------Method 3: DP nottom up----------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1), [0] * (m + 1)]
        

        for i in range(n + 1):
            
            for j in range(m + 1):
                if i==0:
                    f[0][j] = j
                elif j==0:
                    f[i % 2][0] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        f[i % 2][j] = min(f[(i - 1) % 2][j - 1], f[(i - 1) % 2][j] + 1, f[i % 2][j - 1] + 1)
                    # equivalent to f[i % 2][j] = f[(i - 1) % 2][j - 1]
                    else:
                        f[i % 2][j] = min(f[(i - 1) % 2][j - 1], f[(i - 1) % 2][j], f[i % 2][j - 1]) + 1
                        
        return f[n % 2][m]
