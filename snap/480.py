# lazy moving, two heaps can get larger and larger, so wors case is O(NlogN),  best case is O(NlogK)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def move(h1, h2):
            val, i = heapq.heappop(h1)
            heapq.heappush(h2, (-val, i))
            
        def get_med(h1, h2, k):
            if k & 1:
                return h2[0][0]
            else:
                return (-h1[0][0] + h2[0][0]) / 2
        
        small, large = [], []
        res = []
        for i in range(k):
            heapq.heappush(small, (-nums[i], i))
        
        for _ in range(k - (k>>1)):
            move(small, large)
        
        res.append(get_med(small, large, k))
       
        for i, x in enumerate(nums[k:]):
            if x > large[0][0]:
                heapq.heappush(large, (x, i + k))
                if nums[i] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i + k))
                if nums[i] >= large[0][0]:
                    move(small, large)
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            
            res.append(get_med(small, large, k))
        return res
                
        
        
