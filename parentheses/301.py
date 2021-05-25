class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s):
            l, r = 0, 0
            for ch in s:
                if ch == '(':
                    l += 1
                elif ch == ')':
                    if l: l -= 1
                    else: r += 1
            return [l, r]
        def dfs(pos, s, l, r):
            if l == r == 0 and valid(s)[0] == 0 and valid(s)[1] == 0:
                res.append(s)
                return 
            for i in range(pos, len(s)):
                if i != pos and s[i] == s[i - 1]: #同一层
                    continue
                if s[i] == ')' and r:
                    dfs(i, s[:i] + s[i + 1:], l, r - 1)
                elif s[i] == '(' and l:
                    dfs(i, s[:i] + s[i + 1:], l - 1, r)
                
                    
        res = []
        l, r = valid(s)
        dfs(0, s, l, r)
        return res

                    
            
                    
        
