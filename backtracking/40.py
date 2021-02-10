class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(startIndex, target, path, res, visited):
            if target== 0:
                res.append(path[:])
                return 
            if target< 0:
                return 
            for i in range(startIndex, len(candidates)):
                if i in visited:
                    continue
                if i>= 1 and candidates[i]== candidates[i-1] and i-1 not in visited:
                    continue
                visited.add(i)
                dfs(i+ 1, target- candidates[i], path+ [candidates[i]], res, visited)
                visited.remove(i)
                
        candidates= sorted(candidates)
        res= []
        visited= set()
        dfs(0, target, [], res, visited)
        return res
        
                
                    
                
        
        
