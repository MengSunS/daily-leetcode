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
                    
#   BFS


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def validate(s):
            l, r = 0, 0
            for a in s:
                if a == '(':
                    l += 1
                elif a == ')':
                    if l: l -= 1
                    else: r += 1
            return [l, r]
       
        def bfs(s, l, r):
            nonlocal Found
            q = [(s, l, r)]
            nq = []
            seen = set()
            while q:
                for s, l, r in q:
                    if l == 0 and r == 0 and validate(s) == [0, 0]:
                        res.append(s)
                        Found = True
                    if Found:
                        continue
                    for i in range(len(s)):
                        if s[i] == '(' and l and s[:i] + s[i + 1:] not in seen:
                            nq.append((s[:i] + s[i + 1:], l - 1, r))
                            seen.add(s[:i] + s[i + 1:])
                        elif s[i] == ')' and r and s[:i] + s[i + 1:] not in seen:
                            nq.append((s[:i] + s[i + 1:], l, r - 1))
                            seen.add(s[:i] + s[i + 1:])
                q, nq = nq, []
        l, r = validate(s)
        res = []
        Found = False
        bfs(s, l, r)
        return res
                        
                    
