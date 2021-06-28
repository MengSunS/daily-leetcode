class Solution:
    def findRLEArray(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B)
        res = []
        i, j = 0, 0
        while i < m and j < n:
            val, freq = A[i][0] * B[j][0], min(A[i][1], B[j][1])
            A[i][1] -= freq
            if A[i][1] == 0:
                i += 1
            B[j][1] -= freq
            if B[j][1] == 0:
                j += 1
            if not res or res[-1][0] != val:
                res.append([val, freq])
            else:
                res[-1][1] += freq
        return res
            
            
                 
        
