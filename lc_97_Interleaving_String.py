#---Method 1 : dfs+memo---------
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        return self.helper(s1, s2, s3, {})
    
    
    def helper(self, s1, s2, s3, memo):
        if (s1,s2, s3) in memo:
            return memo[(s1,s2, s3)]
        if not s1: return s2==s3
        if not s2: return s1==s3
        if not s1 and not s2 and not s3: 
            return True
        
        memo[(s1, s2, s3)]= False
        
        if s3[-1]==s1[-1]==s2[-1]:
            memo[(s1, s2, s3)]= self.helper(s1[:-1], s2, s3[:-1], memo) or self.helper(s1, s2[:-1], s3[:-1], memo)
            return memo[(s1, s2, s3)]
        elif s3[-1]==s1[-1]:
            
            memo[(s1, s2, s3)]= self.helper(s1[:-1], s2, s3[:-1], memo)
            return memo[(s1, s2, s3)]
                
        elif s3[-1]==s2[-1]:
            memo[(s1, s2, s3)]= self.helper(s1, s2[:-1], s3[:-1], memo)
            return memo[(s1, s2, s3)]
        
        return memo[(s1, s2, s3)]
      
        
                        
        
#----Method 2: DP --------------

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n= len(s1), len(s2)
        if len(s3)!= m+n: return False
        if not s1: return s2==s3
        if not s2: return s1==s3
        dp= [[False]*(n+1) for _ in range(m+1)] # tricky point is use 2D dp stand for the relation among 3 arrays.
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0: 
                    dp[0][j]= s2[:j]==s3[:j]  # easy to forget here
                if j==0:
                    dp[i][0]= s1[:i]==s3[:i] # easy to forget here
                else:
                    if s3[i+j-1]==s1[i-1]==s2[j-1]:  # first i and first j elements, so i+j elemenets, index is: i+j-1
                        dp[i][j]= dp[i-1][j] or dp[i][j-1]
                    elif s3[i+j-1]==s1[i-1]:
                        dp[i][j]= dp[i-1][j]
                    elif s3[i+j-1]==s2[j-1]:
                        dp[i][j]= dp[i][j-1]
        return dp[m][n]
