class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(startIndex, k, n, path):
            if len(path)== k:
                if n== 0:
                    res.append(path)
                return 
                
            for i in range(startIndex, 10):
                if i> n:
                    break
                dfs(i+ 1, k, n- i, path+ [i])
            
        path, res= [], []
        dfs(1, k, n, path)
        return res
                
            
            
        
