class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, res, cnt= 0, -sys.maxsize, 0
        for j in range(len(A)):
            if A[j]==1:
                res= max(res, j-i+1)
            else:
                cnt+= 1
                while cnt> K:
                    if A[i]==0:
                        cnt-= 1
                    i+= 1
                res= max(res, j-i+1)
        return res
                
        
