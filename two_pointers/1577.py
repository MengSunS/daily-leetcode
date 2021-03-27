# Method 1: sort and two and pointers

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return self.helper(nums1, nums2) + self.helper(nums2, nums1)
    
    def helper(self, A, B):
        cnt = 0
        for num in A:
            target = num**2
            i, j = 0, len(B)-1
            
            while i < j:
                if B[i] * B[j] > target:
                    j -= 1
                elif B[i] * B[j] < target:
                    i += 1
                else:
                    if B[i] != B[j]:
                        i0, j0 = i, j
                        while i+1 < j and B[i+1] == B[i]:
                            i += 1
                        print(i, j)
                        while j-1 > i and B[j-1] == B[j]:
                            j -= 1
                        cnt += (i-i0+1) * (j0-j+1)
                        i += 1
                        j -= 1
                    else:
                        cnt += (j-i+1)*(j-i)//2
                        break
        return cnt 
                    
                    
# Method 2: counter, easy brute force

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1 = collections.Counter([num**2 for num in nums1])
        sq2 = collections.Counter([num**2 for num in nums2])
        return self.helper(nums2, sq1) + self.helper(nums1, sq2)
    
    def helper(self, num, sq):
        cnt = 0
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                cnt += sq[num[i]*num[j]]
        return cnt                        
            
