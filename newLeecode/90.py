class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(pos, path):
            res.append(path[:])
            for i in range(pos, n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])
        nums.sort()       
        n = len(nums)
        res = []
        dfs(0, [])
        return res
        
