# 遇到加减乘除符号就总结下已经有的，要看前一个操作符，前一个操作符如果是 + or-，直接用+-当符号把当前的数值丢进stack，如果前一个操作符是*/,从stack里pop出前一个数与当前数*/，再将总结完的数丢到stack里去。最后把stack sum.
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        stack = []
        operator = '+'
        val = 0
        for i in range(n):
            ch = s[i]
            if ch.isdigit():
                val = val * 10 + int(ch)
            if i == n - 1 or not ch.isdigit():
                if operator in {'+', '-'}:
                    stack.append(val if operator =='+' else -val)
                elif operator == '*':
                    stack.append(stack.pop() * val)
                else:
                    prev = stack.pop()
                    if prev / val < 0:
                        stack.append(math.ceil(prev / val))
                    else:
                        stack.append(prev // val)
                operator = ch
                val = 0
        return sum(stack)
                        
                    
                    
                
                
        
        
