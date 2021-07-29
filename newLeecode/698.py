class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(pos, sums, ngrp):
            if ngrp == k:
                return True
            if sums > target:
                return False
            if sums == target:
                return dfs(0, 0, ngrp + 1)
            
            for i in range(pos, n):
                if i not in seen and sums + nums[i] <= target: 
                    seen.add(i) 
                    if dfs(i + 1, sums + nums[i], ngrp):
                        return True
                    seen.remove(i)
            return False
        
        nums.sort(reverse=True)
        n = len(nums)
        if k > len(nums): return False
        if sum(nums) % k != 0: return False
        target = sum(nums) // k
        seen = set()
        return dfs(0, 0, 0)
                    
        
        
