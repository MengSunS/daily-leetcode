class Solution:
    def decodeString(self, s: str) -> str:
        curStr, num, stack = '', 0, []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i].isalpha():
                curStr += s[i]
            elif s[i] == '[':
                stack.append(curStr)
                stack.append(num)
                curStr, num = '', 0
            else:
                n = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + curStr * n  
        return curStr
