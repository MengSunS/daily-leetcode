 # method 1: binary search

# 平均O(logn),最坏O(n)当所有值都一样时
class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = l + (r - l) // 2
            if A[mid] > A[r]:
                l = mid + 1
            elif A[mid] < A[r]:
                r = mid
            else:
                if r - 1 >= 0 and A[r] < A[r - 1]:
                    return A[r]
                    # 这里保证返回的不止是最小值，还是pivot的位置, 只是r -= 1的话会pass the pivot, altho mino values are the same.
                r -= 1
        return A[l]
        


# method 2: recursion, divide and conquer. 最好O(1), 平均O(logn),最坏array值都一样时O(n)


class Solution:
    def findMin(self, A: List[int]) -> int:
        return self.find(A, 0, len(A) - 1)
    def find(self, A, l, r):
        if l == r: 
            return A[l]
        if A[l] < A[r]:
            return A[l]
        mid = l + (r - l) // 2
        return min(self.find(A, l, mid), self.find(A, mid + 1, r) )
        
