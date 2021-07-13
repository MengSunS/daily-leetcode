# Dp, 不是prefix,dp[i] stands for maximum sum ends with nums[i]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)
        return max(dp)
    
    def maxSubArray_better(self, nums: List[int]) -> int:
        n = len(nums)
        curSum = res = nums[0]
        for i in range(1, n):
            curSum = nums[i] + max(curSum, 0)
            res = max(res, curSum)
        return res
    
            
        
