# https://www.youtube.com/watch?v=z7TZ2tLDfuc
#从小到大单调双端队列。找<= presum-K的前面的presum,且index越大（新）越好
#为什么是递增呢? 假设现在有个presum要放进去了，那么如果前面有比它大的，还老，那么一定不会选，
#presum index越大，值越小，越更容易满足（贪心）想选的后面的那一段>=K，所以把比它大的都pop出来；
#当现在有presum时，从左到右找最后一个不满足<= presum- K的，找到之后前面的（包括找到的这个）都可以直接删掉
#这时已经记录了一个区间长度，j再增加时，连这步找到的都不会用，因为区间长度变大了而前面的这步也满足条件，前面的
#更不会用了。

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        presum= 0
        q= collections.deque([(0, -1)])
        res= sys.maxsize
        for j in range(len(A)):
            presum+= A[j]
            while q and q[0][0]<= presum- K:
                res= min(res, j- q[0][1])
                q.popleft()
            while q and q[-1][0]>= presum:
                q.pop()
            q.append([presum, j])
        return res if res!= sys.maxsize else -1
            
        
