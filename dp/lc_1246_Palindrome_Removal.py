class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        if len(arr)==1: return 1
        n= len(arr)
        dp= [[sys.maxsize]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i]= 1
        
        for d in range(1, n):
            for i in range(0, n-d):
                j= i+d
                if arr[i]== arr[j]:
                    if d==1:
                        dp[i][j]= 1
                    else:
                        dp[i][j]= dp[i+1][j-1]
                
                for k in range(i, j):
                    dp[i][j]= min(dp[i][j], dp[i][k]+ dp[k+1][j])
        
        return dp[0][n-1]
