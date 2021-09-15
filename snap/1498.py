# 此题若有重复，index不一样是允许的，如第二个例子。需要跟面试官确认。 
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i <= j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            while i <= j and nums[i] + nums[j] <= target:
                res += pow(2, j - i, MOD)
                i += 1
        return res % MOD
                
        
