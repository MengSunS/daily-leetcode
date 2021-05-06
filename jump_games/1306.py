这题1月份群里做过，当时是在bfs tag下，这次做完二叉树后用recursion的方法，是dfs模板的变形后

# recursion or dfs

class Solution:
    def canReach(self, A: List[int], i: int) -> bool:
        seen = set()
        def helper(i):
            if 0 <= i < len(A) and i not in seen:
                seen.add(i)
                return A[i] == 0 or helper(i + A[i]) or helper(i - A[i])
            return False
        return helper(i)
        
        

Method 1: leetcode 215  recursion 省去seen set空间

class Solution:
    def canReach(self, A: List[int], i: int) -> bool:
        if 0 <= i < len(A) and A[i] >= 0:
            A[i] = -A[i]
            return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i]) 
        return False
        
        
        

Method 2: bfs

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = set()
        while q:
            index = q.popleft()
            if arr[index] == 0:
                return True
            for nxt in [index - arr[index], index + arr[index]]:
                if nxt > len(arr) -1 or nxt < 0:
                    continue
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return False 




