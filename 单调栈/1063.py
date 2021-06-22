class Solution:
    def validSubarrays(self, A: List[int]) -> int:
        stack = []
        res = 0
        for a in A:
            if stack and stack[-1] > a:
                stack.pop()
            stack.append(a)
            res += len(stack)
        return res
    
    
    
