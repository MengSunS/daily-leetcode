# method 1: stack:  https://www.youtube.com/watch?v=fAsV6SIJ-GI

# stack {}思路： 当')'时，总结当前cur的值，当'(',将cur push进stack, cur重置为0重新开始。stack里面是前面算好的值，会在‘)’时pop出来与cur interact
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        cur = 0
        for s in S:
            if s == ')':
                if cur == 0:
                    cur = 1
                else:
                    cur *= 2
                cur += stack.pop()
            else:
                stack.append(cur)
                cur = 0
        return cur

# method 2: recursion  https://www.youtube.com/watch?v=tiAaVfMcL9w

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(l, r):
            if l + 1 == r:
                return 1
            b = 0
            for i in range(l, r):
                if s[i] == '(':
                    b += 1
                if s[i] == ')':
                    b -= 1
                if b == 0:
                    return helper(l, i) + helper(i + 1, r)
            return 2* helper(l + 1, r - 1)
        return helper(0, len(s) - 1)

# method 3: O(1), only to this question calculation definition 

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d = 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == '(':
                d += 1
            if s[i] == ')':
                d -= 1
            if s[i] == '(' and s[i + 1] == ')':
                res += 1 << (d - 1)
               
        return res
    
    # (()) ((()))
    # 2^1 + 2^2
                
        
