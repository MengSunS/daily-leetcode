class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = min(sweetness), sum(sweetness) // (K + 1)
        while l < r:
            mid = (l + r + 1) // 2
            #when want sum at least >= sth,对比当want sum <= sth
            cuts, curSum = 0, 0
            for s in sweetness:
                curSum += s
                if curSum >= mid:
                    cuts += 1
                    curSum = 0
            if cuts < K + 1:
                r = mid - 1
            else:
                l = mid
        return r
        
        
        
