class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(pos, path, value, last):
            if pos == len(num) and value == target:
                res.append(path)
                return 
            
            for i in range(pos, len(num)):
                x = num[pos:i + 1]
                if len(x) >= 2 and x[0] == '0':
                    continue
                x = int(x)
                
                if last is None: #此处不能not last, cuz 0 also satisfies
                    dfs(i + 1, str(x), x, x)
                else:
                    dfs(i + 1, path + '+' + str(x), value + x, x)
                    dfs(i + 1, path + '-' + str(x), value - x, -x)
                    dfs(i + 1, path + '*' + str(x), value - last + last * x, last * x)
        res = []
        dfs(0, '', 0, None)
        return res
       

# 古城verbal的思路，slow + more space

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        combo = []
        self.dfs(0, num, [], combo)
        res = []
        for cand in combo:
            if self.eval(cand) == target:
                res.append(''.join(cand))
        return res
    
    
    def dfs(self, pos, num, path, combo):
        if pos == len(num):
            combo.append(''.join(path[:]))
            return 
        
        for i in range(pos, len(num)):
            if i > pos and num[pos] == '0':
                continue
            if i == len(num) - 1:
                self.dfs(i + 1, num, path + [num[pos:i + 1]], combo)
            else:
                for op in ['+', '-', '*']:
                    self.dfs(i + 1, num, path + [num[pos:i + 1]] + [op], combo)
                
    def eval(self, cand):
        stack = []
        tmp = 0
        operator = '+'
        for i in range(len(cand)):
            cur = cand[i]
            if cur.isdigit():
                tmp = tmp * 10 + int(cur)
            if i == len(cand) -1 or cur in ['+', '-', '*']:
                if operator == '+':
                    stack.append(tmp)
                elif operator == '-':
                    stack.append(-tmp)
                elif operator == '*':
                    stack.append(stack.pop() * tmp)
                operator = cur
                tmp = 0
        
        
        return sum(stack) 
