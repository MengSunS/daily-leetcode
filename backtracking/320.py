class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(index, num, path):
            if index== len(word):
                res.append(path+ str(num) if num>0 else path)
                return 
            
            dfs(index+1, num+1, path)
            dfs(index+1, 0, path+(str(num) if num else '')+word[index])
        res= []
        dfs(0, 0, '')
        return res
