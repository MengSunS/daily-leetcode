class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right, res, summ= 0, 0, sys.maxsize, 0
        for right, num in enumerate(nums):
            summ+= num
            while summ>= s:
                res= min(res, right-left+1)
                summ-= nums[left]
                left+= 1
        
        return res if res!= sys.maxsize else 0
            
        
