--- Lee 215 nb method-----

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res= 0
        
        for a in sorted(arr)[:-1]:
            i= arr.index(a)
            left= arr[i-1] if i-1>=0 else sys.maxsize
            right= arr[i+1] if i+1<len(arr) else sys.maxsize
            res+= min(left, right)*a
            arr.pop(i)
        return res

---DP bottom up method-----

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res= 0
        
        for a in sorted(arr)[:-1]:
            i= arr.index(a)
            left= arr[i-1] if i-1>=0 else sys.maxsize
            right= arr[i+1] if i+1<len(arr) else sys.maxsize
            res+= min(left, right)*a
            arr.pop(i)
        return res
