# Method 1: recursion

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        map= collections.Counter(s)
        res= 0
        flag= 1
        for ch, cnt in map.items():
            if cnt< k:
                flag= 0
                break
        if flag== 1:
            return len(s)            
        
        for i in range(len(s)):
            if map[s[i]]< k: continue
            j= i
            while j< len(s) and map[s[j]]>= k:
                j+= 1
            res= max(res, self.longestSubstring(s[i:j], k))
            i= j
        return res
        
# Method 2: O(26N), 加个condition让右指针能停下来，条件是：unqiue char 个数等于m
# m 个数是从1到26, 也可以最大是s unique 的char个数，每个m是O(N)扫一遍打擂台，外层循环
# m也是打擂台。值得注意的是对于每个m想做的是返回unqiue char个数是m的，每个元素freq
# at least为k的最长的子序列长度。cnt的是freq等于k的元素的个数，当cnt==m时，就是一个candidate

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res= 0
        max_size= len(collections.Counter(s))
        for m in range(max_size+1):
            res= max(res, self.helper(s, m, k))
        return res

    
    def helper(self, s, m, k):
        res= 0
        l= 0
        cnt= 0
        map= {}
        for r in range(len(s)): 
            map[s[r]]= map.get(s[r], 0)+ 1 # 先放
            if map[s[r]]== k:  # at least, k+1, K=2..时就不需要重复加了
                cnt+= 1
            while len(map)> m:
                map[s[l]]-= 1
                if map[s[l]]== k-1: # k-2, k-3..时就不要重复减了
                    cnt-= 1
                if map[s[l]]==0:
                    del map[s[l]]
                l+= 1          
                
            if cnt== m: # 右边界可以继续跑绝对打掉现在的擂台
                res= max(res, r-l+1)
        return res
                
                
            
        
            
               
