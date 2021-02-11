class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        visited= set()
        res= []
        self.dfs(nums, [], res, visited)
        return res
    
    def dfs(self, nums, path, res, visited):
        if len(path)== len(nums):
            res.append(path[:])
            return 
        
        for i in range(len(nums)):
            if i in visited:
                continue
            if i>=1 and nums[i]== nums[i-1] and i-1 not in visited:
                continue
            visited.add(i)
            path.append(nums[i])
            self.dfs(nums, path, res, visited)
            visited.remove(i)
            path.pop()
            
        
        
