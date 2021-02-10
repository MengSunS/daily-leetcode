class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, startIndex, k, path, res):
            if len(path)== k:
                res.append(path[:])
                return 
            for j in range(startIndex, n+1):
                path.append(j)
                dfs(n, j+ 1, k, path, res)
                path.pop()
        res= []
        dfs(n, 1, k, [], res)
        return res
                
        
        
