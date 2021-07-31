# time: O(M + N), M is number of rows, N is number of cols.

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        i, j = 0, n - 1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                j -= 1
        return j + 1 if j != n -1 else -1


# binary search by rows, restrict right pointer by min so far.
# time O(MlogN)


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        min_col = n 
        l, r = 0, n - 1
        for i in range(m):
            while l < r:
                mid = l + (r - l) // 2
                if binaryMatrix.get(i, mid) == 1:
                    r = mid 
                else:
                    l = mid + 1
            if binaryMatrix.get(i, l) == 1:
                min_col = min(min_col, l)
            l, r = 0, (min_col if min_col != n else n - 1)
            
        return min_col if min_col != n else -1 
