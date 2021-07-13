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
                
            
#比较209, positive numbers, return shortest length

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        sums = 0
        i, j = 0, 0
        for j in range(n):
            sums += nums[j]
            while sums >= target:
                res = min(res, j - i + 1)
                sums -= nums[i]
                i += 1
        return res if res != float('inf') else 0
                
