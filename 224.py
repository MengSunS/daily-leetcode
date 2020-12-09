# Method 1: stack+ recursive template

class Solution:
    def __init__(self):
        self.i= -1
    
    def calculate(self, s: str) -> int:
        stack, num, sign= [], 0, 1
      
        while self.i< len(s)-1:
            self.i+= 1
            char= s[self.i]
            
            if char.isdigit():
                num= num*10+ int(char)
            
            if char== '(':  #这个if一定要在下个if前面，（）里算的num才会被放到stack里
                num= self.calculate(s)
              
            if self.i==len(s)-1 or char in {'+', '-', ')'}:
                stack.append(sign*num)
                if char=='+':
                    sign= 1
                elif char=='-':
                    sign= -1
                num= 0

            if char==')':
                break
        ans= 0
        while stack:
            ans+= stack.pop()
        return ans
            
        
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
