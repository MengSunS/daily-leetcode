class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = float('inf')
        l, r = 0, n - 1
        while l + 1 < n and arr[l + 1] >= arr[l]:
            l += 1 
        while r - 1 >= 0 and arr[r - 1] <= arr[r]: #这里写错了,两个typos
            r -= 1
        if l == n - 1: return 0
        res = min(res, r, n - (l + 1))
        for i in range(l + 1):
            while r < n and arr[r] < arr[i]:
                r += 1
            res = min(res, r - i - 1)
        return  res
        
