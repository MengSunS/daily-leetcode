class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign= 0, [], 1
        operator= '+'
        for i in range(len(s)):
            c= s[i]
            if c.isdigit():
                num= num*10+ int(c)
                
            if i==len(s)-1 or c in {'+', '-', '*', '/'}:
                if operator== '+':
                    stack.append(num)
                   
                elif operator== '-':
                    stack.append(-num)
                    
                elif operator== '*':
                    x= stack.pop()
                   # python 正数3//2=1, but 负数-3//2=-2 instead of -1需要特殊处理下先按照正的算 
                    sign= 1 if x>=0 else -1
                    num= sign*(num* abs(x))
                    
                    stack.append(num)
                   
                elif operator=='/':
                    x= stack.pop() 
                    sign= 1 if x>=0 else -1
                    num = sign * (abs(x) // num)
                    stack.append(num)
                    
                num= 0
                operator= c
        
        ans= 0
        while stack:
            ans+= stack.pop()
        return int(ans)
                    
                    
                    
        
