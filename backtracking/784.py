class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(startIndex, path):
            res.append(path)
            if startIndex>= len(S):
                return
            
            for i in range(startIndex, len(path)):
                if path[i].isdigit():
                    continue
                    
                path= path[:i]+ path[i].swapcase()+ path[i+1:]
                dfs(i+ 1, path)
                path= path[:i]+ path[i].swapcase()+ path[i+1:]
                
        res= []
        dfs(0, S)
        return res
