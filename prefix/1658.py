class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0: return n #错在这个没写，涵盖不了此corner case
        prefix = 0
        cache = {0 : -1}
        res = -1
        for i in range(n):
            prefix += nums[i]
            if prefix - target in cache:
                res = max(res, i - cache[prefix - target])
            if prefix not in cache: #这个此题其实不需要写，因为A[i] >= 1
                cache[prefix] = i
        return n - res if res != -1 else -1
    
    
    

