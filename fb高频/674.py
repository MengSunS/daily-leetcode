class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        anchor = 0
        for i in range(n):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            res = max(res, i - anchor + 1)
        return res
            
# another method see leetcode submission 1st        
