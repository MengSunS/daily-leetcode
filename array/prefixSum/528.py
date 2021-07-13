class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1] 
        

    def pickIndex(self) -> int:
        target = self.w[-1] * random.random()
        l, r = 0, len(self.w) - 1
        while l < r:
            mid =  l + (r - l) // 2
            if self.w[mid] < target:
                l = mid  + 1
            else:
                r = mid 
        return l
    
    def pickIndex_slow(self):
        target = self.w[-1] * random.random()
        for i in range(len(self.w)):
            if self.w[i] >= target:
                return i
    
    
         

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
