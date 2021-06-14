class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack, num_map, res= [], {}, []
        
        for num in nums2:
            while stack and stack[-1]< num:
                num_map[stack.pop()]= num
            stack.append(num)
        
        while stack:
            num_map[stack.pop()]= -1
        
        for num in nums1:
            res.append(num_map[num])
            
        return res
