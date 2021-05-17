# 从最矮的开始往里面摸，当前高度小于边上的能存水h-cur，继续摸，边界h不变。
# 假设到一个更高的停了，再pop第二矮的开始摸，若一个点从第一次和第二次均能摸到，
# 会不会该点能存的水其实比第一次多呢？不会，因为联通后会发现取决于最矮的边界
# 而prioty queue就是从矮到高。



class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pq = []
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            for j in range(n):
                if i in {0, m -1} or j in {0, n - 1}:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        
        res = 0
        while pq:
            h, i, j = heapq.heappop(pq)
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if m - 1 > ni > 0 < nj < n - 1 and heightMap[ni][nj] != -1:
                    res += max(h - heightMap[ni][nj], 0)
                    heapq.heappush(pq, (max(h, heightMap[ni][nj]), ni, nj))
                    heightMap[ni][nj] = -1
        return res
        
