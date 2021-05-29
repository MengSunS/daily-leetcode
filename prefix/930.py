class Solution:
    def numSubarraysWithSum(self, A: List[int], t: int) -> int:
        psums = 0
        c = collections.defaultdict(int) # freq map
        c[0] = 1
        res = 0
        for a in A:
            psums += a
            res += c[psums - t]
            c[psums] += 1
        return res
        
        
        
