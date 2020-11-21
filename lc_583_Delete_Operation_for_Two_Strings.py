#----------Method1: dfs + memo-----------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @functools.lru_cache(None)
        def dfs(w1, w2):
            
            if not w1 and not w2:
                return 0
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)

            if w1[-1]== w2[-1]:
                return dfs(w1[:-1], w2[:-1])
            else:
                return min(dfs(w1[:-1], w2), dfs(w1, w2[:-1]))+ 1
        
        return dfs(word1, word2)

           
    
    #---------dfs+ memo---------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dfs(word1, word2, {})
    
    def dfs(self, w1, w2, memo):
        if (w1, w2) in memo:
            return memo[(w1, w2)]
        if not w1 and not w2:
            return 0
        if not w1:
            return len(w2)
        if not w2:
            return len(w1)
        
        if w1[-1]== w2[-1]:
            ans= self.dfs(w1[:-1], w2[:-1], memo)
        else:
            ans= min(self.dfs(w1[:-1], w2, memo), self.dfs(w1, w2[:-1], memo))+ 1
        
        memo[(w1, w2)]= ans
        return memo[(w1, w2)]
        
#--------Method 2: DP-----------------

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n= len(word1), len(word2)
        dp= [[sys.maxsize]*(n+1) for _ in range(2)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[0][j]= j
                elif j==0:
                    dp[i%2][0]= i
                else:
                    if word1[i-1]== word2[j-1]:
                        dp[i%2][j]= dp[(i-1)%2][j-1]
                    else:
                        dp[i%2][j]= min(dp[(i-1)%2][j], dp[i%2][j-1])+1
                        
        return dp[m%2][n]
