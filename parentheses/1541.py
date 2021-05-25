class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = []
        b = 0
        i = 0
        while i < len(S):
            if S[i] == '(':
                b += 1
                i += 1
            elif S[i] == ')':
                if i + 1 <= len(S) - 1 and S[i + 1] == ')':
                    if b > 0:
                        b -= 1
                    else:
                        res += 1
                    i = i + 2
                else:
                    if b > 0:
                        res += 1
                        b -= 1
                    else:
                        res += 2
                    i += 1
              
        res += b* 2
        return res
        
