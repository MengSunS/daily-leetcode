class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack= []
        res= -sys.maxsize
        
        #作为i的可能index: 单调递减的stack,比如[6,4,5]情况，比5大的一定能选前面的4
        for i in range(len(A)):
            if not stack or A[stack[-1]]> A[i]:
                stack.append(i)
        #作为j的可能index,从最大的右边开始（最大range）以内的当然更小了，so最大的range用完直接pop
        for i in range(len(A)-1, -1, -1):
            while stack and A[i]>= A[stack[-1]]:            
                j= stack.pop()
            res= max(res, i-j)
        
        return res
            
  #也可以nlogn 外面循环里面二分法: youtube.com/watch?v=sjaP446Z6bQ      
