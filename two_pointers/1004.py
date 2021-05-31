class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = i = 0
        n = len(nums)
        zeros = 0
        for j in range(n):
            zeros += (nums[j] == 0)
            while zeros > k:
                zeros -= (nums[i] == 0)
                i += 1
            res = max(res, j - i + 1)
        return res
    
       
                
        
