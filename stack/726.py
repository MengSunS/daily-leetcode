# https://www.youtube.com/watch?v=AZZ18B2Spac

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack= []
        cur= {}
        i= 0
        while i< len(formula):
            if formula[i]=='(':            
                stack.append(cur)
                cur= {} 
                i+= 1
               
            elif formula[i]==')':  
                j= i+1
                while j< len(formula) and (formula[j]).isdigit():
                    j+= 1
                num= 0
                if j==i+1:
                    num= 1
                else:
                    num= int(formula[i+1:j])
                for x, cnt in cur.items():
                    cur[x]= cnt*num
                prev= stack.pop()
                for p, cnt in prev.items():
                    cur[p]= cur.get(p, 0)+ cnt
                i= j
            else:
                if formula[i]>='A':
                    j= i+1
                    while j< len(formula) and formula[j]>='a' and formula[j]<='z':
                        j+= 1
                    element= formula[i:j]
                    print('i:'+ str(i)+' //'+element)
                    i= j
                    
                    while j< len(formula) and formula[j].isdigit():
                        j+= 1
                    num= 0
                    if j==i:
                        num= 1
                    else:
                        num= int(formula[i:j])
                    cur[element]= cur.get(element, 0)+ num
                    i= j
                
        ans= ''
        
        for x, cnt in sorted(cur.items()):
            ans+= x
            if cnt>1:
                ans+= str(cnt)
        return ans
                
                
                    
