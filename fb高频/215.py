# method 1, heapq, O(nlogk)

class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        pq = []
        for a in A:
            if len(pq) < k:
                heapq.heappush(pq, a)
            elif a > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, a)
        return pq[0]

# method 2: binary search O(32N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def count(val):
            return sum(num >= val for num in nums)
                 
        l, r = -10 ** 4, 10 ** 4
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= k:
                l = mid
            else:
                r = mid - 1
        return l

# method 3: quick select, average O(n) worst O(n^2)

class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        if not A: return 
        pivot = random.choice(A)
        left = [x for x in A if x > pivot]
        mid = [x for x in A if x == pivot]
        right = [x for x in A if x < pivot]
        L, M, R = len(left), len(mid), len(right)
        
        if L >= k:
            return self.findKthLargest(left, k)
        if L + M < k:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        
