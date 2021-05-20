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
