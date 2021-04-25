# Method 1: dfs


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(pos, path):
            if pos == n:
                res.append(''.join(path[:]))
                return 
            if S[pos].isalpha():
                dfs(pos + 1, path + [S[pos].lower()])
                dfs(pos + 1, path + [S[pos].upper()])
            else:
                dfs(pos + 1, path + [S[pos]])
                
        
        res = []
        n = len(S)
        dfs(0, [])
        return res

# Method 2:  iterator

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(pos, path):
            if pos == n:
                res.append(''.join(path[:]))
                return 
            if S[pos].isalpha():
                dfs(pos + 1, path + [S[pos].lower()])
                dfs(pos + 1, path + [S[pos].upper()])
            else:
                dfs(pos + 1, path + [S[pos]])
                
        
        res = []
        n = len(S)
        dfs(0, [])
        return res

# Method 3: lee215 two liner

class Solution:
    def letterCasePermutation(self, S):
        L = [set([i.lower(), i.upper()]) for i in S]
        return map(''.join, itertools.product(*L))


