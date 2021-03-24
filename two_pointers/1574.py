# https://www.youtube.com/watch?v=pNNvmjNJcu8
class Solution:
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        n = len(A)
        j = n-1
        ret = n-1
        while j-1>=0 and A[j-1]<=A[j]:
            j -= 1
        ret = min(ret, j)
       
        for i in range(n):
            if i-1>=0 and A[i]<A[i-1]: break
            while j<n and A[i]>A[j]:
                j += 1
            ret = min(ret, j-i-1)
        return max(ret, 0)
    
        
