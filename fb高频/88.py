class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        p = m + n - 1
       
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[p] = A[i]
                i -= 1
            else:
                A[p] = B[j]
                j -= 1
            p -= 1
            
        while j >= 0:
            A[p] = B[j]
            j -= 1
            p -= 1
            

   
# or写成：

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        p = m + n - 1
       
        while j >= 0:
            if i >= 0 and A[i] > B[j]:
                A[p] = A[i]
                i -= 1
            else:
                A[p] = B[j]
                j -= 1
            p -= 1
            
        
