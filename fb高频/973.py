class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x ** 2 + y ** 2, x, y) for x, y in points]
        self.quickSelect(0, len(dist) - 1, dist, k)
        return [[x, y] for _, x, y in dist[:k]]
    
    def quickSelect(self, s, e, dist, k):
        if s >= e:
            return 
        l, r = self.partition(s, e, dist)
        if k < r + 1: #个数，左边界点（包含）以左无序但符合条件
            self.quickSelect(s, r, dist, k)
        if k >= l + 1: #个数，右边界点（包含）以右无序大于pivot
            self.quickSelect(l, e, dist, k)
    
    def partition(self, l, r, dist):
        pivot = dist[l + (r - l) // 2][0]
        while l <= r:
            while dist[l][0] < pivot:
                l += 1
            while dist[r][0] > pivot:
                r -= 1
            if l <= r:
                dist[l], dist[r] = dist[r], dist[l]
                l += 1
                r -= 1 #这俩个习惯性忘写,不是whole sequence完全的partition
        return l, r
            
        
            
        
