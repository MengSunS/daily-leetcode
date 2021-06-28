class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B)
        i = j = 0
        res = []
        while i < m and j < n:
            s = max(A[i][0], B[j][0])
            e = min(A[i][1], B[j][1])
            if s <= e:
                res.append([s, e])
            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
                j += 1
        return res
        
