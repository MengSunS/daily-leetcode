# hash map

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vals = {i : val for i, val in enumerate(nums) if val}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        m, n = len(self.vals), len(vec.vals)
        res = 0
        if m > n:
            self.vals, vec.vals = vec.vals, self.vals
        for k, v in self.vals.items():
            res += v * vec.vals.get(k, 0)
        return res

# tuple and two pointers 

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vals = [(i, val) for i, val in enumerate(nums) if val]
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        print(self.vals, vec.vals)
        i, j = 0, 0
        m, n = len(self.vals), len(vec.vals)
        res = 0
        while i < m and j < n:
            if self.vals[i][0] == vec.vals[j][0]:
                res += self.vals[i][1] * vec.vals[j][1]
                i += 1
                j += 1
            elif self.vals[i][0] > vec.vals[j][0]:
                j += 1
            else:
                i += 1
        return res
                

# array

class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(self.arr)):
            res += self.arr[i] * vec.arr[i]
        return res
        
