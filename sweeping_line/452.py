# official solution, sort by ending points:

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        
        return arrows

# my own: sort by starting points, find # of overlaps

class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        if not A: return 0
        A.sort()
        cnt = 1
        n = len(A)
        prev = A[0]
        for i in range(n):
            start, end = A[i][0], A[i][1]
            if start > prev[1]:
                prev = A[i]
                cnt += 1
            else:
                prev = [max(prev[0], start), min(prev[1], end)]
        return cnt


