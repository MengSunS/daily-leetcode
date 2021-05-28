# optimal method: O(n)


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        f = collections.defaultdict(int)
        f[0] = 1
        sums = collections.defaultdict(int)
        prefix = 0
        res = 0

        for i in range(n):
            prefix ^= arr[i]
            res += f[prefix] * i - sums[prefix]
            sums[prefix] += i + 1
            f[prefix] += 1
        return res
            
            
            
       
# O(n^2)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xors = [0] * (n + 1)
        res = 0
        for i in range(n):
            xors[i + 1] = xors[i] ^ arr[i]
            
        for i in range(n):
            for k in range(i + 1, n):
                if xors[i] == xors[k + 1]:
                    res += k - i 
        return res

# O(n^3)

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xors = [0] * (n + 1)
        res = 0
        for i in range(n):
            xors[i + 1] = xors[i] ^ arr[i]
            
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = xors[i] ^ xors[j]
                    b = xors[j] ^ xors[k + 1] 
                    if a == b:
                        res += 1
        return res
                      
