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
                        
                        
                    
# O(1) space, use res and prev, when current s[i] in {'+', '-'}, update prev into res

class Solution:
    def calculate(self, s: str) -> int:
        res, prev, num, sign = 0, 0, 0, '+'
        for i, a in enumerate(s):
            if a.isdigit():
                num = num * 10 + int(a)
            if i == len(s) - 1 or a in {'+', '-', '*', '/'}:
                if sign == '+':
                    prev = num
                elif sign == '-':
                    prev = -num
                elif sign == '*':
                    prev *= num
                else:
                    if prev / num >= 0:
                        prev //= num
                    else:
                        prev = math.ceil(prev / num)
                if a in {'+', '-'}: #关键是这行
                    res += prev
                    prev = 0    
                sign, num = a, 0
            else:
                continue
        return res + prev
                        
                        
                    
                
