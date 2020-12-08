class Solution:
    def simplifyPath(self, path: str) -> str:
        stack= []
        for s in path.split('/'):
            if stack and s =='..':
                stack.pop()
            if s not in {'.', '..', ''}:
                stack.append(s)
        
        return '/'+'/'.join(stack)
                
        
