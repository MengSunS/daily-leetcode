class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base = tmp = extra = 0
        n = len(customers)
        for i in range(n):
            if not grumpy[i]:
                base += customers[i]
            else:
                tmp += customers[i]
            if i >= X:
                tmp -= customers[i-X] * grumpy[i-X]
            extra = max(extra, tmp)
            
        return base + extra
                
        
