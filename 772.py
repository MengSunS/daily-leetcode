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
            
            if self.i== len(s)-1 or c in {'+', '-', '*', '/', ')'}:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    x= stack.pop()
                    sign_x= 1 if x>= 0 else -1
                    stack.append(sign_x*(abs(x)*num))
                elif operator == '/':
                    x= stack.pop()
                    sign_x= 1 if x>= 0 else -1
                    stack.append(sign_x*(abs(x)//num))
                num= 0
                operator= c
                
            if c ==')':
                break
        
        ans= 0
        while stack:
            ans+= stack.pop()
        return ans
                
                
                    
