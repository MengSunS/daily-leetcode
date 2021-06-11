class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        mini, res = inf, inf
        for num in nums:
            cur = -num if num % 2 == 0 else -num * 2
            heapq.heappush(pq, cur)
            mini = min(mini, -cur)
            
        while pq[0] % 2 == 0:
            res = min(res, -pq[0] - mini)
            mini = min(mini, -pq[0] // 2)
            heapq.heappushpop(pq, pq[0] // 2)
            
        return min(res, -pq[0] - mini)
    
        


        
            
        
