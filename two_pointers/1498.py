

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        res = 0
        i, j = 0, len(nums)-1
        while i<= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += pow(2, j-i, mod)
                i += 1
        return res % mod
        
