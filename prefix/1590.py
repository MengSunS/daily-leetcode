# 这题主要用到余数的性质，余数运算没有分配律，但是有这个：
# (a - b) % p = (a % p - b % p) % p
#这里的a就是rolling prefixsum， b就是sub array，a-b就是在cache里的prefixsum
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cache = {0: -1}
        target = sum(nums) % p
        prefix = 0
        n = len(nums)
        res = n
        for i in range(n):
            prefix = (prefix + nums[i]) % p
            cache[prefix] = i # 不能算完更新，因为当前可能就满足
            if (prefix - target) % p in cache:
                res = min(res, i - cache[(prefix - target) % p])
            
        return res if res < n else -1
                
        # A + B = C
        # ?    B%p   cur
        # (C - B) % p = (C% p - B % p) % p
        # A % p = (cur - target) % p
        # cache
        
