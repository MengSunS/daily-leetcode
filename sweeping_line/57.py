class Solution:
    def insert(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        i, n = 0, len(A)
        s, e = B[0], B[1]
        res = []
        # 1st step, add intervals before the new interval directly into res using start < new start, pointer ends at next interval in the old list
        while i < n and A[i][0] < s:
            res.append(A[i])
            i += 1
        # 2nd step, merge or add the new interval based on last res end vs. new start
        if not res or res[-1][1] < s:
            res.append(B)
        else:
            res[-1][1] = max(res[-1][1], e)
        # 3rd step, transform into merge intervals
        while i < n:
            if res[-1][1] < A[i][0]:
                res.append(A[i])
            else:
                res[-1][1] = max(res[-1][1], A[i][1])
            i += 1
        return res
                
        
