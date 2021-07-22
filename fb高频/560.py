# if both positive & negativ exist

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
                


# if all positive
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, res, cur = 0, 0, 0
        
        for j in range(n):
            cur += nums[j]
            while cur > k:
                cur -= nums[i]
                i += 1
            if cur == k:
                res += 1
        return res
            
