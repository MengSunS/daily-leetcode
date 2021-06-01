 # j - i 而非j - i - 1的原因是包含从i + 1, i + 2..j之间的，除了min i是必须的，下一步是i += 1,这时不记下来单独的i就错过了；== 和< 公共用else而非单独开两行的原因是：test case可能有重复的数，所以右边固定时，左边下一个也满足
    
        

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
        
