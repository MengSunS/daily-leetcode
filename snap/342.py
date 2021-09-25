class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num   


    def isPowerOfFour(self, num: int) -> bool:
        if num < 0 : return False
        def helper(num):
            if num < 4:
                if num == 1:
                    return True
                else:
                    return False
            return helper(num/4)
        return helper(num)
    
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0 : return False
        while num >= 4:
            num /= 4
        return num == 1
                    
