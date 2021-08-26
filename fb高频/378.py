class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(pq)
        for _ in range(k):
            res, i, j = heapq.heappop(pq)
            if j < len(matrix[0]) - 1:
                heapq.heappush(pq, (matrix[i][j + 1], i, j + 1))
        return res


# binary search
# time: binary log(max-min), within each binary search, O(N) time to count number of elements less than or equal to mid. So overall, O(N) * log(max - min). 

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = l + (r - l) / 2
            lo, hi = float('-inf'), float('inf')
            count, lo, hi = self.countLessEqual(matrix, mid, lo, hi)
            if count == k:
                return lo
            elif count < k:
                l = hi # 边界总是在matrix中 (因为最后返回的是l or r), mid可以是hypothetical
            else:
                r = lo
        return l
    
    def countLessEqual(self, matrix, mid, lo, hi):
        n = len(matrix)
        row, col = n - 1, 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                hi = min(hi, matrix[row][col])
                row -= 1
            elif matrix[row][col] <= mid:
                count += row + 1
                lo = max(lo, matrix[row][col])
                col += 1 #这里比较难想，从下往上，到了一个可以的，直接往上消消乐加法，col直接jump到右边，因为下面的大于，下面的右边更大于，直接skip.
        return count, lo, hi
                
        
                
