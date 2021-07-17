class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(pq)
        for _ in range(k):
            res, i, j = heapq.heappop(pq)
            if j < len(matrix[0]) - 1:
                heapq.heappush(pq, (matrix[i][j + 1], i, j + 1))
        return res
        
