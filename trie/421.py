class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res= 0
        for i in range(31, -1, -1):
            res<<= 1
            prefix= {num>>i for num in nums}
            nxt= res | 1
            if any(p^nxt in prefix for p in prefix):
                res= nxt
        return res
