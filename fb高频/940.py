class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] *26
        for ch in s:
            end[ord(ch) - ord('a')] = sum(end) + 1
        return sum(end) % (10 ** 9 + 7)
                
        
