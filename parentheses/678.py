class Solution:
    def checkValidString(self, S: str) -> bool:
        cmin, cmax = 0, 0 # cmin, all * --> r; cmax, all * --> l
        for s in S:
            if s == ')':
                cmin -= 1
                cmax -= 1
            elif s == '(':
                cmin += 1
                cmax += 1
            else:
                cmax += 1
                cmin -= 1
            if cmax < 0:
                return False
            if cmin < 0:
                cmin += 1
        return cmin == 0
    
       
        
