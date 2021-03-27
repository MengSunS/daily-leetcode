# or, notice i, j end condition

class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        i = j = k
        n = len(A)
        res, mini = A[k], A[k]
        while i > 0 or j < n-1:
            if (A[i - 1] if i else 0) > (A[j + 1] if j < n-1 else 0):
                i -= 1
            else:
                j += 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j-i+1))
            
        return res
       
        
            
                
                
# and

class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        i = j = k
        n = len(A)
        res, mini = A[k], A[k]
        while i > 0 and j < n-1:
            if A[i - 1] > A[j + 1]:
                i -= 1
            else:
                j += 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j - i + 1))
                
        while i> 0:
            i -= 1
            mini = min(mini, A[i])
            res = max(res, mini * (j - i + 1))
            
        while j < n-1:
            j += 1
            mini = min(mini, A[j])
            res = max(res, mini * (j - i + 1))
        return res
       
        
            
                
                
            
            
            
        
