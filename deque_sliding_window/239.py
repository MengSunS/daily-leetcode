
# https://www.youtube.com/watch?v=2SXqBsTR6a8

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack= collections.deque([])
        res= []
        for i in range(len(nums)):
            if stack and stack[0][1]== i-k:
                stack.popleft()
                
            while stack and stack[-1][0]< nums[i]:
                stack.pop()
            
            stack.append([nums[i], i])
            if i>=k-1:
                res.append(stack[0][0])
        return res
                
            
        
