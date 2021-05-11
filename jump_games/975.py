像高中数学题

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_lower, next_higher = [0] * n, [0] * n
        
        stack = []
        for a, i in sorted([(a, i) for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for a, i in sorted([(-a, i) for i, a in enumerate(A)]):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        
        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n-1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        
        return sum(higher)
            
            
            
        
        
                
        
        
