class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getKWords(i):
            k = 0
            l = ' '.join(words[i:i+k])
            while len(l) <= maxWidth and i + k <= n:
                k += 1
                l = ' '.join(words[i:i+k])
            return k - 1
             
        def insertSpace(i, k):
            l = ' '.join(words[i: i + k])
            if k == 1 or i + k == n:
                needs = maxWidth - len(l)
                line = l + ' ' * (needs)
            else:
                needs = maxWidth - len(l) + k - 1
                even, left = divmod(needs, k - 1)
                if left > 0:
                    line = (' ' * (even + 1)).join(words[i: i + left])
                    line += ' ' * (even + 1)
                    line += (' ' * even).join(words[i + left: i + k])         
                else:
                    line = (' ' * even).join(words[i: i + k])
            return line
     
        n = len(words)
        i = 0    
        res = []
        while i < n:
            k = getKWords(i)
            line = insertSpace(i, k)
            res.append(line)
            i += k
        return res
        
        
        
        
        
