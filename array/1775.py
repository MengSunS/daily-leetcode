class Solution:
    def minOperations(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if 6 * m < n or m > 6 * n: return -1
        sums1, sums2 = sum(A), sum(B)
        if sums1 > sums2: A, B = B, A # A sum is smaller
        counter = collections.Counter([6 - a for a in A] + [b - 1 for b in B])
        target = abs(sums2 - sums1)
        d = 5
        res = 0
        while target > 0:
            while counter[d] == 0:
                d -= 1
            target -= d
            counter[d] -= 1
            res += 1
        return res
            
            
        
            
# method 2: sort and two sum, time is worse O(nlogn), but if is sorted already, space is better

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        sums1, sums2 = sum(nums1), sum(nums2)
        target = abs(sums2 - sums1)
        if sums1 > sums2:
            nums1, nums2 = nums2, nums1 # nums1 if smaller one
        m, n = len(nums1), len(nums2)
        if 6 * m < 1 * n: 
            return -1
        i, j = 0, n - 1
        cnt = 0
        while target > 0 and (i < m or j > 0):
            print(i, j)
            if 6 - nums1[i] > nums2[j] - 1 or j == -1:
                target -= 6 - nums1[i]
                i += 1
            elif 6 - nums1[i] <= nums2[j] - 1 or i == m:
                target -= nums2[j] - 1
                j -= 1
            cnt += 1
        return cnt        
        
