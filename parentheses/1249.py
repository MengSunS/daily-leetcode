# stack里放open brackets index. string is imutable, convert into list
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s= list(s)
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
            
        
