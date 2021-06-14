class Solution:
    
    def findTargetSumWays(self, nums, s):
        if len(nums) == 0:
            return 0
        
        memo = {}
        return self.dfs(0, 0, nums, s, memo)
    
    def dfs(self, startIndex, curSum, nums, target, memo):
        if (startIndex, target - curSum) in memo:
            return memo[(startIndex, target - curSum)]

        if startIndex == len(nums): 
            if curSum == target:
                return 1
            return 0

        ways = 0
        ways += self.dfs(startIndex + 1, curSum + nums[startIndex], nums, target, memo)
        ways += self.dfs(startIndex + 1, curSum - nums[startIndex], nums, target, memo)
        memo[(startIndex, target - curSum)] = ways
        return ways

            
