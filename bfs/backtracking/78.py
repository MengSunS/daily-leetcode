class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, startIndex, path, res):
        # here dont judge if startIndex==sth, cuz will need all the paths along the way 
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i+ 1, path, res) # i+ 1 not startIndex
            path.pop()
        
