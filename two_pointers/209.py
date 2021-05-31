class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, i = 0, 0
        n = len(nums)
        res = inf
        for j in range(n):
            s += nums[j]
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1
                
        return res if res != inf else 0
                
        
        
