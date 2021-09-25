class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = nums
        for i in range(1, len(nums)): 
            prefix[i] += prefix[i-1]

        ans = 0
        for i in range(len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            ans += max(0, min(len(nums) - 1, k) - max(i+1, j))
            
        return ans % 1_000_000_007

