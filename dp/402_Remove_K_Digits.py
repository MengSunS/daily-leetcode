class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
       
        if len(num)==k: return '0'
        n= len(num)
        stack= []
        for i in range(n):
            while stack and stack[-1]> num[i] and len(stack)-1-i>= -k:
                stack.pop()
            if len(stack)< n-k:
                stack.append(num[i])
        
        return str(int(''.join(stack)))
    
    

        
        
        
        
