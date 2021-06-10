class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            sums = 0
            b = max(a - index, 0)
            sums += (a + b) * (a - b + 1) / 2
            c = max(a - (n - 1 - index), 0)
            sums += (a + c) * (a - c + 1) / 2
            return sums - a
        
        maxSum -= n
        l, r = 0, maxSum
        while l < r:
            mid = l + (r - l + 1) // 2
            if test(mid) <= maxSum:
                l = mid 
            else:
                r = mid - 1
        return l + 1
        
        
                
        
