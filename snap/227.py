class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
        for i, a in enumerate(s):
            if a.isdigit():
                num = num * 10 + int(a)
            if i == len(s) - 1 or a in {'+', '-', '*', '/'}:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    temp = stack.pop()
                    if temp / num >= 0:
                        stack.append(temp // num)
                    else:
                        stack.append(math.ceil(temp / num))
                sign, num = a, 0
            else:
                continue
        return sum(stack)
                        
                        
                    
        
