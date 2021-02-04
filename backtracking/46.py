class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited= set()
        res= []
        n= len(nums)
        self.dfs(nums,  [], res, visited, n)
        return res
    
    def dfs(self, nums, path, res, visited, n):
        if len(path)== n:
            res.append(path[:])
            return 
        
        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            path.append(nums[i])
            self.dfs(nums, path, res, visited, n)
            visited.remove(i)
            path.pop()
            
        
