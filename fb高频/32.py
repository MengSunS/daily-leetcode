class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [] # index of (, and index of unpaired ) as wall
        res = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    if stack: 
                        res = max(res, i - stack[-1])
                    else: 
                        res = i + 1
                else:
                    stack.append(i)
                    
        return res
    
    
        

        
      
        
