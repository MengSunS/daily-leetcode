# 不是sliding window, 答案的left指针可能为0. score - (score - 1) = 1
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score, res = 0, 0
        seen = {}
        for i, h in enumerate(hours):
            score += (1 if h > 8 else -1)
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score <= 0:
                res = max(res, i - seen.get(score - 1, float('inf')))
        return res
            
        
