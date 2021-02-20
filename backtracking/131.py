class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(Index, path):
            if Index== len(s):
                res.append(path)
                return 
            for i in range(Index, len(s)):
                cand= s[Index: i+1]
                if cand== cand[::-1]:
                    dfs(i+1, path+ [cand])
        res, path= [], []
        dfs(0, path)
        return res
    
    
