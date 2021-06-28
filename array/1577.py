class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def find(target, B):
            cnt = 0
            seen = collections.defaultdict(int)
            for b in B:
                if target % b == 0:
                    cnt += seen.get(target // b, 0)
                seen[b] += 1
            return cnt 
        
        @lru_cache(None)
        def twoProduct1(target):
            return find(target, nums1)
        
        @lru_cache(None)
        def twoProduct2(target):
            return find(target, nums2)
        
       
        return sum(twoProduct1(val ** 2) for val in nums2) + sum(twoProduct2(val ** 2) for val in nums1) 
                    
    
                
   Two sum --> Two product: 

method 1: using map, O(n ^ 2). one list loop target, each target, O(N) find cnt; space O(m + n) map
method 2: two pointers, sort O(nlogn), sort完也是O(n ^ 2), 总体时复不变. space O(1)
method 3: 一开始写的方法. one list into counter, another list two loops find cnt, O(n  ^ 3), space O(m + n)

method 2空间更优.     
