# meet in the middle, divide array into two halves, and binary search

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(pos, cur, nums, sums):
            sums.add(cur)
            for i in range(pos, len(nums)):
                dfs(i + 1, cur + nums[i], nums, sums)
         
        nums0, nums1 = nums[:len(nums)//2], nums[len(nums)//2:]
        l_sums, r_sums =  set(), set()
        dfs(0, 0, nums0, l_sums)
        dfs(0, 0, nums1, r_sums)
        r_sums = sorted(r_sums)
        
        ans = float('inf')
        for x in l_sums:
            i = bisect_left(r_sums, goal - x)
            if i < len(r_sums):
                ans = min(ans, r_sums[i] + x - goal)
            if i > 0:
                ans = min(ans, abs(r_sums[i - 1] + x - goal))
        return ans
                
                
            
        
        
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def fn(nums):
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans
        
        nums0 = sorted(fn(nums[:len(nums)//2]))
        ans = inf
        for x in fn(nums[len(nums)//2:]): 
            k = bisect_left(nums0, goal - x)
            if k < len(nums0): ans = min(ans, nums0[k] + x - goal)
            if 0 < k: ans = min(ans, goal - x - nums0[k-1])
        return ans 
                        
        
