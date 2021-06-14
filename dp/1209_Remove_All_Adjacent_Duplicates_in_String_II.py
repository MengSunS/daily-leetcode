class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack= []
        for char in s:
            if not stack:
                stack.append([char, 1])
            else:
                if stack and stack[-1][0]== char:
                    stack[-1][1]+= 1
                    if stack[-1][1]==k: #把这个if写在嵌套里会省些判断时间
                        stack.pop()
                else:
                    stack.append([char, 1])
        
        res= ''
        for v, t in stack:
            res+= (v*t)
        
        return res
        
                    
                
            
            
        
        
