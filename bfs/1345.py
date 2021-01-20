class Solution:
    def minJumps(self, arr: List[int]) -> int:
        map= defaultdict(list)
        for i, v in enumerate(arr):
            map[v].append(i)
        q= deque([(0, 0)])
        seen= set()
        seen.add(0)
        n= len(arr)
        while q:
            idx, dist= q.popleft()
            if idx== n-1:
                return dist
            num= arr[idx]
            for next_idx in [idx- 1, idx+ 1]+ map[num]:
                if next_idx not in seen and 0<=next_idx<n:
                    seen.add(next_idx)
                    q.append((next_idx, dist+1))
            map[num]= []  
        
        # same values的index用完一次后下一次就可以剪枝了，因为总可以通过上一次直接跳到那个位置
            
        
                
            
        
