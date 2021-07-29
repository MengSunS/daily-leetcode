class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(pos, path):
            if len(path) >= 2:
                res.add(tuple(path[:]))
            for i in range(pos, n):
                if path and nums[i] >= path[-1] or not path:
                    dfs(i + 1, path + [nums[i]])
       
        n = len(nums)
        res = set()
        dfs(0, [])
        return res
    

