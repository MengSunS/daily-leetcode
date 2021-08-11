# lc158

class Solution:
    def __init__(self):
        self.q = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                buf4 = [''] * 4
                v = read4(buf4)
                if v == 0:
                    break
                self.q.extend(buf4)
        return i
                    
        
        
# lc157 O(1) space

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            buf4 = [''] * 4
            v = read4(buf4)
            count = min(n - i, v)
            if count == 0:
                break
            buf[i:] = buf4[:count]
            i += count
        return i
