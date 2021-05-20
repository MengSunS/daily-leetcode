# 

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        @lru_cache(None)
        def dfs(i, j):
            if s[i: j + 1].isdigit():
                return [int(s[i: j + 1])]
            res = []
            for k in range(i, j+1):
                c = s[k]
                if c in '*+-':
                    l = dfs(i, k - 1)
                    r = dfs(k + 1, j)
                    res.extend([eval(str(x)+c+str(y)) for x in l for y in r]) #笛卡尔积
            return res
        
        n = len(s)
        return dfs(0, n - 1)









class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)
    
    def dfs(self, s, m):
        if s in m:
            return m[s]
        if s.isdigit():
            m[s] = [int(s)]
            return m[s]
        res = []
        for i, c in enumerate(s):
            if c in '*+-':
                l = self.dfs(s[:i], m)
                r = self.dfs(s[i+1:], m)
                res.extend([eval(str(x)+c+str(y)) for x in l for y in r]) #笛卡尔积
        m[s] = res
        return m[s]
