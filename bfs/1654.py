class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        seen= set()
        seen.add((0, False))
        q= deque([(0, False)])
        limit= max(forbidden)+ x+a+b
        forbidden= set(forbidden)
        res= 0
        while q:
            
            for _ in range(len(q)):
                pos, is_last_backward= q.popleft()
                print(pos)
                if pos== x:
                    return res
                
                # jump forward
                nxt_pos= pos+ a
                if nxt_pos not in forbidden and nxt_pos< limit and (nxt_pos, False) not in seen:
                    q.append((nxt_pos, False))
                    seen.add((nxt_pos, False))
                # jump backward
                if not is_last_backward:
                    nxt_pos= pos- b
                    if nxt_pos not in forbidden and nxt_pos>=0 and (nxt_pos, True) not in seen:
                        q.append((nxt_pos, True))
                        seen.add((nxt_pos, True))
                 
            res+=1
        return -1
