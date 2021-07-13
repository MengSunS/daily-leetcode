class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        preSum = 0
        res = 0
        for i, a in enumerate(nums):
            preSum += a
            res += seen.get(preSum - k, 0)
            seen[preSum] = seen.get(preSum, 0) + 1
        return res
                
            
        
