# One stack. 存tuple [x, y], y是目前为止最小的, y轴也是递减的
# deque 用doubly linked list实现，不需要连续memmory space, however geting ramdon indexing takes O(n) time, 
# but stack does not call random indexing, so deque is better than list in this question. List uses continous
# memory allocation. 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque() 
        
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(val, self.stack[-1][1])])
            

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return 
    
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
i

# method 2, 1 stack, another is montonic decreasing one 

def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mono = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono or self.mono[-1] >= val:
            self.mono.append(val)
        

    def pop(self) -> None:
        num = self.stack.pop()
        if self.mono[-1] == num:
            self.mono.pop()
        
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mono[-1]
