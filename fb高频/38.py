# 题意： (i + 1) count and say ith result
# Method 1: iterative

class Solution:
    def countAndSay(self, n: int) -> str:
        # itertaive意会下怎么上一次的结果是这一次的输入，这么简单直白还看不懂啊？
	res = '1'
        for i in range(n - 1): # itertaive: say it how many times: n - 1 times
            res = self.next(res)
        return res
    
    def next(self, s):
        i = 0
        n = len(s)
        res = ''
        while i < n:
            cnt = 1
            while i + 1 < n and s[i + 1] == s[i]:
                i += 1
                cnt += 1
            res += str(cnt) + s[i]
            i += 1
        return res
        
    
# Method 2: recursive

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.say(self.countAndSay(n - 1))
    
    def say(self, s):
        i = 0
        res = ''
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i + 1] == s[i]:
                count += 1
                i += 1
            res += str(count) + s[i]
            i += 1
        return res

# 有点divide and conquer（但面试要说recursion,因为不是对半divide）的思想。题意是

# 1     2                 3                 4
# '1'   f(2)=say('1')  f(3)=say(f(2))      say(f(3))

# 其中，f是本题定义的函数。

# So naturally, return say(f(n - 1)),触底的是f(1) == '1'.
