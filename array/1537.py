class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        sums1, sums2 = 0, 0
        m, n = len(A), len(B)
        i, j = 0, 0
        while i < m or j < n:
            if i < m and (j == n or A[i] < B[j]):
                sums1 += A[i]
                i += 1
            elif j < n and (i == m or A[i] > B[j]):
                sums2 += B[j]
                j += 1
            else:
                sums1 = sums2 = max(sums1, sums2)
                sums1 += A[i]
                sums2 += B[j]
                i += 1
                j += 1
        return max(sums1, sums2) % (10 ** 9 + 7)
                
        
        
