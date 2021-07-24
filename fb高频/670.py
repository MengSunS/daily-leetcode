class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        c = {x: i for i, x in enumerate(A)}
        for i, a in enumerate(A):
            for b in range(9, a, -1):  
                if c.get(b, -1) > i:
                    A[c[b]], A[i] = A[i], A[c[b]]       
                    return int(''.join(map(str, A)))
        return num
         
        
