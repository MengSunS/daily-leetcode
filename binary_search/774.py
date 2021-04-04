class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        l, r = 1e-6, stations[-1] - stations[0]
        while l + 1e-6 < r:
            mid = (l + r) / 2
            need = 0
            for a, b in zip(stations, stations[1:]):
                # if b - a > mid:
                #     if (b - a) % mid != 0:
                #         need += (b - a) // mid
                #     else:
                #         need += (b - a) // mid - 1
                        
                need += math.ceil((b - a)/mid) - 1
            if need > k:
                l = mid + 1e-6
            else:
                r = mid
        return l 
        
        
