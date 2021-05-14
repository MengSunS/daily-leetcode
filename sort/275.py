# Method 1: log(n)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2  # [0, 1] -> 0
            if n - mid > citations[mid]:
                l = mid + 1
            else:
                r = mid 
        
        if n - l <= citations[l]:
            return n - l
        else:
             return 0
       
# Scan one time  O(n):


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i, c in enumerate(citations):
            if c >= n - i:
                return n - i
        return 0
        
