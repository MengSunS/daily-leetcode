class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        abbrs= []
        self.dfs(0, [], 0, abbrs, target)
        abbrs.sort(key=len)
        dictionary= set(dictionary)
        for abbr in abbrs:
            # all(item_list), return True when all item in list is True
            if all([not self.check_match(abbr, word) for word in dictionary]):
                return ''.join(abbr)
        return False
    
    def dfs(self, pos, path, cnt, res, target):
            if pos== len(target):
                res.append(path+([str(cnt)] if cnt>0 else []))
                return 
            cand= [target[pos]]
            self.dfs(pos+1, path+ ([str(cnt)] if cnt else [])+ cand, 0,  res, target)
            self.dfs(pos+1, path, cnt+1, res, target)
        
    
    def check_match(self, abbr, word):
        # use two pointers to check whether is able to be matched
        i= j= 0
        while True:
            if i==len(abbr) and j==len(word): return True
            if i>= len(abbr) or j>= len(word): return False
            if abbr[i].isdigit():
                step= int(abbr[i])
                i+= 1
                j+= step
            else:
                if abbr[i]!= word[j]: return False
                i+= 1
                j+= 1
        return True
        
       
        
