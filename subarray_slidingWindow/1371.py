class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx= {0: -1}
        vowels= 'aeiou'
        state= 0
        ans= 0
        
        for i, char in enumerate(s):
            j= vowels.find(char)
            if j>=0:
                state^= 1<<j
            if state not in idx:
                idx[state]= i     
            ans= max(ans, i- idx[state]) # 可以省略else,因为事先不存在的话上行已经放入
        return ans 
        
        
