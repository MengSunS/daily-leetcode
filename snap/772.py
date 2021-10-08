class Solution:
    def calculate(self, s: str) -> int:
        s += '#'
        def helper(stack, i):
            num, sign = 0, '+'
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                elif s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    num, i = helper([], i + 1)
                else:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    else:
                        stack.append(int(stack.pop() / num))
                    if s[i] == ')':
                        return sum(stack), i + 1
                    else:
                        sign, num = s[i], 0
                        i += 1
            return sum(stack)
        return helper([], 0)
            
        class Solution:
    def calculate(self, s: str) -> int:
        s = s + '#'
        def helper(stack, i):
            num, sign = 0, '+'
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                elif s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    num, i = helper([], i + 1)
                else:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)   
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    else:
                        stack[-1] = int(stack[-1] / num)
                    if s[i] == ')':
                        return sum(stack), i + 1
                    else:
                        sign = s[i]
                        num, i = 0, i + 1
            return sum(stack)
        
        return helper([], 0)
                
            
        
