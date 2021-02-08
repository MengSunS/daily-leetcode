class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(startIndex):
            if len(path)== len(digits):
                res.append(''.join(path[:]))
                return 
            for s in num2str[digits[startIndex]]:
                path.append(s)
                dfs(startIndex+ 1)
                path.pop()
                
        if not digits: return []
        path, res= [], []
        num2str= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        dfs(0)
        return res

