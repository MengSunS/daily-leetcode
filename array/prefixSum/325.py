class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        preSum = 0
        res = 0
        for i, a in enumerate(nums):
            preSum += a
            if preSum - k in seen:
                res = max(res, i - seen[preSum - k])
            seen.setdefault(preSum, i)
        return res 
            
        
