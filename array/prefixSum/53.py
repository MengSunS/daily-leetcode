class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)
        return max(dp)
    
    def maxSubArray_DP_better(self, nums: List[int]) -> int:
        n = len(nums)
        curSum = res = nums[0]
        for i in range(1, n):
            curSum = nums[i] + max(curSum, 0)
            res = max(res, curSum)
        return res

    def maxSubArray_prefixSum(self, nums: List[int]) -> int:
        preSum = 0
        miniSum = 0
        res = float('-inf')
        for i, a in enumerate(nums):
            preSum += a
            res = max(res, preSum - miniSum)
            miniSum = min(miniSum, preSum)
        return res

    def maxSubArray_greedy(self, nums: List[int]) -> int:
        res = float('-inf')
        preSum = 0
        for a in nums:
            preSum += a
            res = max(res, preSum)
            preSum = max(preSum, 0)
        return res
    
   
    
            
        
