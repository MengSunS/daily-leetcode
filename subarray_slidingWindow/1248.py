class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums= [num%2 for num in nums]
        prefix= 0
        map= {0: 1}
        res= 0
        for num in nums:
            prefix+= num
            res+= map.get(prefix-k, 0)
            map[prefix]= map.get(prefix, 0)+ 1
        
        return res
                
        
