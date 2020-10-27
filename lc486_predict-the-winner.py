class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo= {}
        return self.maximum_difference(nums, 0, len(nums)-1, memo)>= 0
    
    def maximum_difference(self, nums, l, r, memo):
        if (l, r) in memo:
            return memo[l, r]
        if l==r:
            return nums[l]
        
        memo[l, r]= max(nums[l]- self.maximum_difference(nums, l+1, r, memo), nums[r]- self.maximum_difference(nums, l, r-1, memo))
 
        return memo[l, r]
        
