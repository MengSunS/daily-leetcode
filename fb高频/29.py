class Solution:
    def divide(self, a: int, b: int) -> int:
        sign = 1
        if a < 0: sign *= -1
        if b < 0: sign *= -1
        a, b = abs(a), abs(b)
        res = 0
        while a >= b:
            tmp = b
            times = 1
            while (tmp << 1) <= a:
                tmp = (tmp << 1)
                times = (times << 1)
            res += times
            a -= tmp
        
        if sign * res >= 2 ** 31:
            return 2 ** 31 - 1
        return sign * res
                
                
            
        
