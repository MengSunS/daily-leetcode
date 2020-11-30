class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr= [-sys.maxsize]+ arr
        stack= [0]
        res= [0]*len(arr)
        
        for i in range(1, len(arr)):
            #stack里永远是保持着递增序列的index
            while stack and arr[stack[-1]]> arr[i]:
                stack.pop()
            
            j= stack[-1] 
            stack.append(i)
            res[i]= res[j]+ (i-j)*arr[i]
        
        return sum(res)% (10**9 + 7)
            
            
        
