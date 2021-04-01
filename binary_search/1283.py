class Solution:
    def smallestDivisor(self, A: List[int], threshold: int) -> int:
        l, r = 1, max(A)
        while l < r:
            mid = (l + r) // 2
            # if sum((i + m - 1) // m for i in A) > threshold:
            if sum(math.ceil(i / mid) for i in A) > threshold:
                l = mid + 1
            else:
                r = mid
        return l

