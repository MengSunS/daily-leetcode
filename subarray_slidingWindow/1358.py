class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        map= {}
        i= 0
        res= 0
        N= len(s)
        
        for j in range(N):
            map[s[j]]= map.get(s[j], 0)+ 1
            while 'a' in map and 'b' in map and 'c' in map:
                res+= N-j
                map[s[i]]-= 1
                if map[s[i]]==0:
                    del map[s[i]]
                i+= 1
        return res
            
            
                
        
