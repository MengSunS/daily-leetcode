
--------Method 1: dp: bottom up----------

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        dp0, dp1= 0, nums[0]
       
        
        for i in range(2, len(nums)+1):
            dp= max(dp0+nums[i-1], dp1)
            dp0= dp1
            dp1= dp
        
        return dp1
       

-----Method 2: top down recursion----------

class Solution:
    def rob(self, nums: List[int]) -> int:

        return self.dfs(nums, len(nums)-1, {})
    
    def dfs(self, nums, index, memo):
        if index==0:
            memo[0]= nums[0]
            return memo[0]
        if index< 0:
            memo[index]= 0
            return memo[index]
        if index in memo:
            return memo[index]
        
        memo[index]= max(self.dfs(nums, index-2, memo)+ nums[index], self.dfs(nums, index-1, memo))
        return memo[index]
