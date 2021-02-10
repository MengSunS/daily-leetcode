class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(startIndex, target, path, res):
            if target== 0:
                res.append(path)
                return 
            
            if target< 0:
                return 
            
            for i in range(startIndex, len(candidates)):
                if candidates[i]> target:
                    break
                    
                if i> startIndex and candidates[i]== candidates[i-1]:
                    continue
                    
                dfs(i+ 1, target- candidates[i], path+ [candidates[i]], res)
                
        candidates.sort()
        res= []
        dfs(0, target, [], res)
        return res
