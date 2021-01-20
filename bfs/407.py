class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n= len(heightMap), len(heightMap[0])
        directions= {(0,1),(0,-1),(1,0),(-1,0)}
        if m==0: return 0
        hp= []
        seen= set()
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:  
                    if (i,j) not in seen:
                        heapq.heappush(hp, (heightMap[i][j], i, j))
                        seen.add((i,j))

        res= 0
        while hp:
            h, i, j= heapq.heappop(hp)
            for di, dj in directions:
                ni, nj= i+di, j+dj
                if ni>=m or ni<0 or nj>=n or nj<0:
                    continue
                if (ni, nj) in seen:
                    continue
                if  heightMap[ni][nj]<= h: 
                    seen.add((ni, nj))
                    res+= h- heightMap[ni][nj]
                    heapq.heappush(hp, (h, ni, nj))
                elif heightMap[ni][nj]> h: 
                    seen.add((ni, nj))
                    heapq.heappush(hp, (heightMap[ni][nj], ni, nj))          
        return res
                        
