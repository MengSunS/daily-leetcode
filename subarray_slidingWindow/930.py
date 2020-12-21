# Method 1---prefixsum

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        map= {0:1}
        res= 0
        prefix= 0
        
        for a in A:
            prefix+= a
            res+= map.get(prefix- S, 0)
            map[prefix]= map.get(prefix, 0)+ 1
        return res


# Method 2------atMost()

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMost(x):
            if x < 0:
                return 0
            l, r, prefix, res=0, 0, 0, 0
            for r in range(len(A)):
                prefix+= A[r]
                while prefix> x:
                    prefix-= A[l]
                    l+= 1
                res+= r-l+1
            return res
        return atMost(S)- atMost(S-1)
                   
                
         
        
