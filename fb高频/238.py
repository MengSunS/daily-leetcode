# left to me, right to me
class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        p, n = 1, len(A)
        res = []
        for i in range(n):
            res.append(p)
            p *= A[i]
        p = 1
        for j in range(n - 1, -1, -1):
            res[j] *= p
            p *= A[j]
        
        return res
            
