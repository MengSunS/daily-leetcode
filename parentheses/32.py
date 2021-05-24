class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    if not stack:
                        res = max(res, i + 1)
                    else:
                        res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        maxi = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                else:
                    dp[i] = 0
                    
            maxi = max(maxi, dp[i])
        return maxi
            
