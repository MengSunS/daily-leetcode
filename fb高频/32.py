# Method 1: stack

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
    
  

# Method 2: DP

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(': # dp[i - 1] xxx
                    dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0) 
                         
        return max(dp) if dp else 0
                    
                    
                        
                
        
        
      
        
