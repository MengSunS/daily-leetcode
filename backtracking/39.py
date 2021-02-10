class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, startIndex, target, path, res):
            if target== 0:
                res.append(path[:])
                return 
            if target< 0:
                return 
            for i in range(startIndex, len(candidates)):
                dfs(candidates, i, target- candidates[i], path+ [candidates[i]], res)
                
        res= []
        dfs(candidates, 0, target, [], res)
        return res
        
