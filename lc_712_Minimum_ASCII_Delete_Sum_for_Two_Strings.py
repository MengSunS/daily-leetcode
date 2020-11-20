#----Method 1: dfs+ memo  写的垃圾的一批-----
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        return self.dfs(s1, s2, {}, {})
    
    def dfs(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if not s1 and not s2:
            return 0
        elif not s1:     
            memo[(s1, s2)]= sum(ord(char) for char in s2)
        elif not s2:
            memo[(s1, s2)]= sum(ord(char) for char in s1)
        else:
            
            if s1[-1]==s2[-1]:
                ans= self.dfs(s1[:-1], s2[:-1], memo)
            else:
                ans= min(self.dfs(s1[:-1], s2, memo)+ ord(s1[-1]), self.dfs(s1, s2[:-1], memo)+ ord(s2[-1]), self.dfs(s1[:-1], s2[:-1], memo)+ ord(s1[-1])+ ord(s2[-1]))
            memo[(s1, s2)]= ans
        
        return memo[(s1, s2)]
            
        
#------------Method 2: DP--------------
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n= len(s1), len(s2)
        dp= [[sys.maxsize]*(n+1) for _ in range(m+1)]
        dp[0][0]= 0
        
        
        for i in range(1, m+1):
            dp[i][0]= dp[i-1][0]+ ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j]= dp[0][j-1]+ ord(s2[j-1])
        #把这两行写出下面的循环是缩减时间的    
       
        for i in range(1, m+1):
            for j in range(1, n+1):
                
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= dp[i-1][j-1]

                dp[i][j]= min(dp[i][j], dp[i-1][j]+ ord(s1[i-1]), dp[i][j-1]+ ord(s2[j-1]))

        return dp[m][n]
