# convert into sliding window, smallest subarry has k unqiue types. jbut wasted the condition each list is sorted. 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        A = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                A.append((nums[i][j], i))
        A.sort()
        seen = {}
        i = 0
        l, r = float('-inf'), float('inf')
        for j in range(len(A)):
            seen[A[j][1]] = seen.get(A[j][1], 0) + 1
            while len(seen) == len(nums):
                if A[j][0] - A[i][0] < r - l:
                    l, r = A[i][0], A[j][0]
                seen[A[i][1]] -= 1
                if seen[A[i][1]] == 0:
                    del seen[A[i][1]]
                i += 1
        return [l, r]
            
                
# heapq method, gurantee pq always has k values from k lists in it. updating left and right

class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:
        pq = [(A[i][0], i, 0) for i in range(len(A))]
        heapify(pq)
        ans = [float('-inf'), float('inf')]
        max_val = max([A[i][0] for i in range(len(A))])
        
        while pq:
            cur, i, j = heapq.heappop(pq)
            if max_val - cur < ans[1] - ans[0]:
                ans = cur, max_val
            if j + 1 == len(A[i]):
                return ans
            heapq.heappush(pq, (A[i][j + 1], i, j + 1))
            max_val = max(max_val, A[i][j + 1])
