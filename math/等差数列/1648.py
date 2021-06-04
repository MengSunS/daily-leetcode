class Solution:
    def maxProfit(self, A: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7
        A.sort(reverse=True)
        A.append(-1)
        res, k, n = 0, 1, len(A)
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                if k * (A[i] - A[i + 1]) < orders:
                    res += (A[i] + A[i + 1] + 1) * (A[i] - A[i + 1]) // 2 * k
                    orders -= (A[i] - A[i + 1]) * k
                else:
                    h, r = divmod(orders, k)
                    res += (A[i] + A[i] - h + 1) * h // 2 * k + r * (A[i] - h)
                    return res % MOD
                res %= MOD
            k += 1
            
            
       
