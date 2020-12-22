# 思路：state表示uoiea对应是odd(1) 或者even(0)，如果同一state出现两次，表示这中间是个合法的，因为出现又消失抵消了。
# 抵消是用XOR bitmask flip的


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
        
        
