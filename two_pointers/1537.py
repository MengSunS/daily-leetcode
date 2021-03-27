class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        mod = 10**9 + 7
        m, n = len(A), len(B)
        i, j = 0, 0
        res, tmp1, tmp2 = 0, 0, 0
        while i < m and j < n: 
            if A[i] < B[j]:
                tmp1 += A[i]
                i += 1
                
            elif A[i] > B[j]:
                tmp2 += B[j]
                j += 1
                
            else:
                res += max(tmp1, tmp2) + A[i]
                print(A[i], tmp1, tmp2, res)
              
                tmp1, tmp2 = 0, 0
                i += 1
                j += 1
    
        while i < m:
            tmp1 += A[i] 
            i += 1
        while j < n:
            tmp2 += B[j]
            j += 1
            
        res += max(tmp1, tmp2)
           
        return res % mod
                
                
            
        
