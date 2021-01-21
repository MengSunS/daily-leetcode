class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        def flip(state, x, y):
            for dx, dy in [(1, 0),(0, 1),(-1, 0),(0, -1),(0, 0)]:
                nx, ny= x+ dx, y+ dy
                if nx>=m or nx<0 or ny>=n or ny<0:
                    continue
                state^= 1<<(nx*n+ ny) #XOR flip, 2D->1D coordinate: i*n+j
            return state
    
        seen= set()
        m, n= len(mat), len(mat[0])
        start= 0
        q= deque()
        for i in range(m):
            for j in range(n):
                start+= mat[i][j]<<(i*n+j)
        seen.add(start)
        q.append((start, 0))
        while q:
            state, step= q.popleft()
            if state==0:
                return step
            for i in range(m):
                for j in range(n):
                    next_state= flip(state, i, j)
                    if next_state in seen:
                        continue
                    seen.add(next_state)
                    q.append((next_state, step+1))
        return -1
    
    
