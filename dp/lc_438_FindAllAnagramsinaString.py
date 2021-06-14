class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res= []
        
        m, n= len(s), len(p)
        
        for i in range(m-n+1):
            if i==0:
                map_s= collections.Counter(s[:n])   
            else: 
                map_s[s[i-1]]-= 1
                if map_s[s[i-1]]== 0:
                    del map_s[s[i-1]]
                if s[i+n-1] not in map_s:
                    map_s[s[i+n-1]]= 0
                map_s[s[i+n-1]]+= 1
            
            if map_s== collections.Counter(p):
                res.append(i)
        
        return res
                
        
