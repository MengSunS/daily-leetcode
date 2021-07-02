class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        deque, res = collections.deque(), []
        for i in range(len(A)):
            if deque and deque[0][1] == i - k:
                deque.popleft()
            while deque and A[i] >= deque[-1][0]:
                deque.pop()
            deque.append((A[i], i))
            if i >= k - 1:  
                res.append(deque[0][0])
        return res
            
        
        
