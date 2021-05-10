class Solution:
    def minJumps(self, arr: List[int]) -> int:
        map_index = defaultdict(list)
        for i, a in enumerate(arr):
            map_index[a].append(i)
        
        q = deque([(0, 0)])
        stack = []
        seen = {0}
        while q:
            for idx, steps in q:
                if idx == len(arr) - 1 :
                        return steps
                for nxt in [idx + 1, idx -1] + map_index[arr[idx]]:
                    if 0 <= nxt < len(arr) and nxt not in seen:
                        seen.add(nxt)
                        stack.append((nxt, steps + 1))
                    if nxt == len(arr) -1 :
                        return steps + 1
                map_index[arr[idx]]= []  
            q, stack = stack, []
            
