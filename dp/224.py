# Method 1: stack+ recursive template
class Solution:
    def __init__(self):
        self.i= -1
        
    def calculate(self, s: str) -> int:
        stack, num, operator= [], 0, '+'
        
        while self.i< len(s)-1:
            self.i+= 1
            c= s[self.i]
            if c.isdigit():
                num= num*10+ int(c)
            if c== '(':
                num= self.calculate(s)
            if self.i== len(s)-1 or c in {'+', '-', ')'}:
                if operator=='+':
                    stack.append(num)
                else:
                    stack.append(-num)
                num= 0
                operator= c
            if c==')':
                break
        
        return sum(stack[:])
            
                
                
        
        
                   
        
# Method 2: stack 

class Solution:
    def calculate(self, s: str) -> int:
        stack= []
        res, num, sign= 0, 0, 1
        
        for i in range(len(s)):
            char= s[i]
            if char.isdigit():
                num= num*10+ int(char)
            elif char in {'+', '-'}:
                res+= sign*num
                num= 0
                sign= 1 if char=='+' else -1
            elif char== '(':
                stack.append(res)
                stack.append(sign)
                num, res, sign= 0, 0, 1
                
            elif char==')':
                res+= sign*num
                res= stack.pop()*res+stack.pop()
                num, sign= 0, 1
        res+= num*sign
        return res
