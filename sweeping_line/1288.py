# offcial solution
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: (x[0], -x[1]))
        prev_end = 0
        cnt = 0
        
        for _, end in A:
            if end > prev_end:
                cnt += 1
                prev_end = end
        return cnt
       


# my own
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort()
        n = len(A)
        last = A[0]
        cnt = 1
        for i in range(1, n):
            if A[i][0] > last[0] and A[i][1] > last[1]:
                last = A[i]
                cnt += 1
            elif A[i][1] > last[1]:
                last = A[i]
        return cnt 
