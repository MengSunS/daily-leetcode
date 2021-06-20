# aim 情况是最小的打头，however,后面个数不够了就别pop了，直接append上去吧
class Solution:
    def mostCompetitive(self, A: List[int], k: int) -> List[int]:
        stack = []
        for i, a in enumerate(A):
            while stack and stack[-1] > a and len(stack) - 1 + len(A) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack
