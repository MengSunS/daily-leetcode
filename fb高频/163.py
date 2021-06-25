class Solution:
    def findMissingRanges(self, A: List[int], lower: int, upper: int) -> List[str]:
        A = [lower - 1] + A + [upper + 1]
        res  = []
        for i in range(len(A) - 1):
            if A[i + 1] - A[i] == 2:
                res.append(str(A[i] + 1))
            elif A[i + 1] - A[i] > 2:
                res.append(str(A[i] + 1) + '->' + str(A[i + 1] - 1))
        return res
                
        
