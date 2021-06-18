class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        stack = []
        n = len(A)
        res = [-1] * n
        for i in list(range(n)) * 2:
            while stack and A[stack[-1]] < A[i]:
                res[stack.pop()] = A[i]
            stack.append(i)
        return res
        
