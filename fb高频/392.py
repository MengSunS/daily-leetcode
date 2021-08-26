class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        m, n = len(s), len(t)
        while i < m and j < n:
            if t[j] != s[i]:
                j += 1
            else:
                i += 1
                j += 1
        return i == m
    # time好像也是o(m + n),最坏n也要全走一遍
    
    #观点纠正：subsequence不用在乎是否要 abc,出现acabc的情况，第一个a总是有效的，不是mixed continous subarray的
    def isSubsequence_guangtou(self, s: str, t: str) -> bool:
        remainder_t = iter(t)
        for c in s:
            if c not in remainder_t:
                return False
        return True
    # guangtou time O(m + n),两个都要走一遍
        
