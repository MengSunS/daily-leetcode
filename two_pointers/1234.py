# find shortest subarray safities outside the window all count <= n / 4
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        i = 0
        res = n + 1
        # cnt = {c: 0 for c in 'QWER'}
        cnt = collections.Counter(s)
        for j in range(n):
            cnt[s[j]] -= 1
            while i < n and all(cnt[c] <= n / 4 for c in 'QWER'):
                res = min(res, j - i + 1)
                cnt[s[i]] += 1
                i += 1
            # res = min(res, j - i + 2)
        return res
    
    # 注释里的是错误的。这是因为：1）在意的是区间外面的是否可以，而非窗口里面的，判断时需要用外面的；2）while 里面的已经(yi jing)合法的，取个最小的，不要想放在外面
        
