class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        def getNwords(pos):
            n = 0
            acc_len = 0
            for i in range(pos, len(words)):
                acc_len += len(words[i])
                n += 1
                if acc_len + (n - 1) > maxWidth:
                    n -= 1
                    acc_len -= len(words[i])
                    break 
            return n, acc_len
        
        def getLine(pos, n, acc_len):
            if n == 1 or pos + n - 1== len(words) - 1:
                l = ' '.join(words[pos:pos + n])
                line = l + ' ' * (maxWidth - len(l))
            else:
                d, extra = (maxWidth - acc_len) // (n - 1), (maxWidth - acc_len) % (n - 1)
                line = ''
                for i in range(pos, pos + n):
                    line += words[i]
                    if i != pos + n - 1:
                        line += ' ' * d
                    if extra:
                        line += ' '
                        extra -= 1
            return line
        
        def dfs(pos):
            if pos == len(words):
                return 
            n, acc_len = getNwords(pos)
            line = getLine(pos, n, acc_len)
            res.append(line)
            dfs(pos + n)
            
            
        dfs(0)
        return res
            
                
       
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
        
        
        
        
        
