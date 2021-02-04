class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        visited= set()
        res= []
        self.dfs(nums, 0, visited, [], res)
        return res
    
    def dfs(self, nums, startIndex, visited, path, res):
        res.append(path[:])
        
        for i in range(startIndex, len(nums)):
            if i>= 1 and nums[i]==  nums[i-1] and (i-1) not in visited:
                continue
            path.append(nums[i])
            visited.add(i)
            self.dfs(nums, i+1, visited, path, res)
            visited.remove(i)
            path.pop()
            
