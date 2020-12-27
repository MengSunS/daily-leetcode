# https://www.youtube.com/watch?v=5Ec68Qr2GTM

# 本题代码看起来跟lc340很像，只是atMost相减，但思考过程有个小gap,340是求最长substring with at most k
# distinct chars, 自然可以右边界j直接拉到最远，不满足条件了再动i,需要res= max(res, j-i+1),j在拉远的过程中小的会
# 被后面的打掉；
# 而此题是求所有at most k distinct的substring个数，那么在一边走右边界在满足的情况下累加j-i+1（不再是打擂）, j-i+1
# 是包含index为j的数的所有区间的个数，前面有j-i个，再加上j上的数本身，正好为j-i+1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMost(A, K)- self.atMost(A, K-1)
    
    def atMost(self, A, k):
        cnt= 0
        map= {}
        i= 0
        for j in range(len(A)):
            map[A[j]]= map.get(A[j], 0)+ 1
            while len(map)> k:
                map[A[i]]-= 1
                if map[A[i]]==0:
                    del map[A[i]]
                i+= 1
            cnt+= j-i+1
        return cnt
            
        
