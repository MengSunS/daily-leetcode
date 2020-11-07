-------思维1： 按照多边形边数bottom up 轮回切pizza -----

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n= len(A)
        dp= [[0]*n for _ in range(n)]
        
        for d in range(3, n+1):
            for i in range(0, n+1-d):
                j= i+ d-1
                dp[i][j]= sys.maxsize
                for k in range(i+1, j):
                    dp[i][j]= min(dp[i][j], dp[i][k]+ dp[k][j]+ A[i]*A[j]*A[k])
        return dp[0][n-1]
        

------思维2： 按照右边坐标退回去切pizza ---------

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp= [[0]*len(A) for _ in range(len(A))]
        
        for j in range(2, len(A)):
            for i in range(j-2, -1, -1):
                dp[i][j]= float('inf')
                for k in range(i+1, j):
                    dp[i][j]= min(dp[i][j], dp[i][k]+ dp[k][j]+ A[i]*A[j]*A[k])
        return dp[0][len(A)-1]
        
