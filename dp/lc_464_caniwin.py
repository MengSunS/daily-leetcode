class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger* (maxChoosableInteger+1)/2< desiredTotal:
            return False
        if desiredTotal<=0: return True
        nums= [i for i in range(1, maxChoosableInteger+1)]
        memo= {}
        return self.dfs(nums, desiredTotal, memo)

    def dfs(self, nums, T, memo):
        if T<=0: return False
        if tuple(nums) in memo: return memo[tuple(nums)]
        
        for i in range(len(nums)):
            if not self.dfs(nums[:i]+nums[i+1:], T-nums[i], memo):
                memo[tuple(nums)]= True
                return memo[tuple(nums)]
        
        memo[tuple(nums)]= False
        return memo[tuple(nums)]
            
        
