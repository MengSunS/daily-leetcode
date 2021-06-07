class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def check(t):
            return sum([v if v <= t else t for v in arr])
        
        l, r = 0, max(arr)
        while l < r: # the largest th makes sum < target
            mid = l + (r - l + 1) // 2
            if check(mid) <= target:
                l = mid # <时也是合理解
            else:
                r = mid - 1

        if abs(check(l) - target) <= abs(check(l + 1) - target):
            return l
        else:
            return l + 1
    
    
        
   class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def check(t):
            return sum([v if v <= t else t for v in arr])
        
        l, r = 0, max(arr)
        while l < r: # the smaller th makes sum > target
            mid = l + (r - l) // 2
            if check(mid) < target:
                l = mid + 1
            else:
                r = mid 

        if abs(check(l) - target) < abs(check(l - 1) - target):
            return l
        else:
            return l - 1
    
    
        
        class Solution:
    def findBestValue(self, A: List[int], target: int) -> int:
        A.sort(reverse=1)
        maxA = A[0]
        while A and A[-1] * len(A) <= target:
            target -= A.pop()
        return round((target - 0.0001) / len(A)) if A else maxA
    
    # min_num * len(arr) > target, we now know there is a number less than min_num which is the answer
            
        
             
