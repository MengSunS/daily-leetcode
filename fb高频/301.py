class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = self.validate_paren(s)
        res = []
        self.dfs(0, s, l, r, res)
        return res
    
    def dfs(self, pos, path, l, r, res):
        if l == r == 0:
            l0, r0 = self.validate_paren(path)
            if l0 == r0 == 0:
                res.append(path)
                return 
        
        for i in range(pos, len(path)):
            cur = path[i]
            if i > pos and path[i] == path[i - 1]:
                continue
            if cur == '(' and l:
                self.dfs(i, path[:i]+path[i+1:], l - 1, r, res)
                # self.dfs(i + 1, path, l, r, res) # 错在这
            elif cur == ')' and r:
                self.dfs(i, path[:i]+path[i+1:], l, r - 1, res)
                # self.dfs(i + 1, path, l, r, res) # 错在这
    
    def validate_paren(self, s):
        l, r = 0, 0
        for a in s:
            if a == '(':
                l += 1
            elif a == ')':
                if l: l -= 1
                else: r += 1
        return l, r
                    
        
