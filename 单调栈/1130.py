# Method 1: O(n), next greater element, on the right and on the left

class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for a in A:
            while stack and stack[-1] <= a:
                mid = stack.pop()
                res += min(stack[-1], a) * mid
            stack.append(a)
            
        while len(stack) > 2: #当A本来就是单调递减
            mid = stack.pop()
            res += stack[-1] * mid
        return res
                
        
# Method 2: O(n^2)

class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0
        for a in sorted(A)[:-1]:
            print(a)
            i = A.index(a)
            left = A[i - 1] if i - 1 >= 0 else float('inf')
            right = A[i + 1] if i + 1 < len(A) else float('inf')
            res += min(left, right) * a
            A.pop(i)
        return res
                
