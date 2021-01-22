class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n= len(forest), len(forest[0])
        q= [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j]> 1]
        heapq.heapify(q)
        res= 0
        i, j= 0, 0
        
        while q:
            h, x, y= heapq.heappop(q)
            print(h)
            step= self.bfs(forest, i, j, x, y)
            if step== -1:
                return -1
            res+= step
            i, j= x, y
        return res
    
    def bfs(self, forest, i, j, x, y):
        seen= set((i, j))
        m, n= len(forest), len(forest[0])
        directions= [(0,1),(1,0),(0,-1),(-1,0)]
        q= deque([(i, j, 0)])
        while q:
            i, j, step= q.popleft()
            if (i, j)== (x, y):
                return step
            for di, dj in directions:
                ni, nj= i+ di, j+ dj
                if ni< 0 or ni>= m or nj< 0 or nj>= n:
                    continue
                if forest[ni][nj]==0:
                    continue
                if (ni, nj) in seen:
                    continue
                else:
                    q.append((ni, nj, step+1))
                    seen.add((ni, nj))
       
        return -1
            
            
            
            
        
        
