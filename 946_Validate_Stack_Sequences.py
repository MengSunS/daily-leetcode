class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack= []
        popped= collections.deque(popped)
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]== popped[0]:
                stack.pop()
                popped.popleft()
              
        return stack== []
        
