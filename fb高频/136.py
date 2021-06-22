class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
    
    # if x > 0: x ^ 0 = x, x^ x = 0
    # x ^ y ^ x = x^ x ^ y= 0 ^ y = y XOR的交换律
       
