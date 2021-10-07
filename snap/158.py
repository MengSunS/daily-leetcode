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
                num = read4(buf4)
                if num == 0:
                    break
                self.q.extend(buf4[:num])
        return i


# 157

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        q = deque()
        i = 0
        while i < n:
            if q:
                buf[i] = q.popleft()
                i += 1
            else:
                buf4 = [''] * 4
                num =  read4(buf4)
                if num == 0:
                    break
                q.extend(buf4[:num])
        return i

# O(1) space for 157

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
            num = read4(buf4)
            if num == 0:
                break
            count = min(n - i, num)
            buf[i:] = buf4[:count]
            i += count
        return i
