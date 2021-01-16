class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        steps= 0
        q=deque(['0000'])
        visited= set()
        visited.add('0000')
        deadends= set(deadends)
        steps= 0
        while q:
            for _ in range(len(q)):
                cur= q.popleft()
                if cur==target:
                    return steps
                if cur in deadends:
                    continue
                for i in range(4):
                    for dc in {1, -1}:
                        c= (int(cur[i])+ dc)%10
                        nxt= cur[:i]+ str(int(c))+ cur[i+1:]
                        if nxt in visited: continue
                        visited.add(nxt)
                        q.append((nxt))
            steps+= 1
        return -1
    
    # 数层数需加for _ in range(len(q))
    # Or, 将steps加入tuple: (cur, steps)
    
    
                    
#如下：

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        steps= 0
        q=deque(['0000'])
        visited= set()
        visited.add('0000')
        deadends= set(deadends)
        steps= 0
        while q:
            for _ in range(len(q)):
                cur= q.popleft()
                if cur==target:
                    return steps
                if cur in deadends:
                    continue
                for i in range(4):
                    for dc in {1, -1}:
                        c= (int(cur[i])+ dc)%10
                        nxt= cur[:i]+ str(int(c))+ cur[i+1:]
                        if nxt in visited: continue
                        visited.add(nxt)
                        q.append((nxt))
            steps+= 1
        return -1
    
    # 数层数需加for _ in range(len(q))
    # Or, 将steps加入tuple: (cur, steps)
    
    
                    
# tuple:

def openLock(self, deadends: List[str], target: str) -> int:
        steps= 0
        q=deque([('0000',0)])
        visited= set()
        visited.add('0000')
        deadends= set(deadends)
        while q:
            cur, step= q.popleft()
            if cur==target:
                return step
            if cur in deadends:
                continue
            for i in range(4):
                for dc in {1, -1}:
                    c= (int(cur[i])+ dc)%10
                    nxt= cur[:i]+ str(int(c))+ cur[i+1:]
                    if nxt in visited: continue
                    visited.add(nxt)
                    q.append((nxt, step+1))
        return -1            
        
        
