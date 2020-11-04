class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp= [[0]*len(A) for _ in range(len(A))]
        
        for j in range(2, len(A)):
            for i in range(j-2, -1, -1):
                dp[i][j]= float('inf')
                for k in range(i+1, j):
                    dp[i][j]= min(dp[i][j], dp[i][k]+ dp[k][j]+ A[i]*A[j]*A[k])
        return dp[0][len(A)-1]
        
