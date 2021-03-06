class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        l, r = 0, n - 1
        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1
        if l > r:
            return 0
        mini, maxi = min(nums[l:r + 1]), max(nums[l:r + 1]) 
        while l >= 0 and nums[l] > mini:
            l -= 1
        while r <= n - 1 and nums[r] < maxi:
            r += 1
        return r - l - 1
        
        
# lee215, short but O(nlogn)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
        
        
               
