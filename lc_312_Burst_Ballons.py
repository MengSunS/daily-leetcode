class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums= [1]+ nums+ [1]
        n= len(nums)
        dp= [[0]*n for _ in range(n)]
        
        for j in range(1, n-1):
            for i in range(j, 0, -1):
                for k in range(i, j+1):
                    dp[i][j]= max(dp[i][j], dp[i][k-1]+ dp[k+1][j]+ nums[k]*nums[i-1]*nums[j+1])
        
        return dp[1][n-2]
        
