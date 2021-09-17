class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        for i, h in enumerate(heights+[0]):
            while stack and h <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                ans = max(ans, width * height)
            stack.append(i)
        return ans
        
