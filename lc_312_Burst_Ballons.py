-----思路1：先fix区间长度--------

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums= [1]+ nums+ [1]
        n= len(nums)
        dp= [[0]*n for _ in range(n)]
        
        for d in range(2, n):
            for i in range(0, n-d):
                j= i+d
                for k in range(i+1, j):
                    dp[i][j]= max(dp[i][j], dp[i][k]+ dp[k][j]+ nums[k]* nums[i]* nums[j])
                    
        return dp[0][n-1]
                


-----思路2：----------

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
        
