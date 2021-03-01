class WordFilter:

    def __init__(self, words: List[str]):
        self.table= {}
        for idx, word in enumerate(words):
            pre, suf= [], []
            for i in range(len(word)):
                pre.append((pre[-1] if pre else "")+ word[i])
                suf.append(word[len(word)-1-i]+ (suf[-1] if suf else ""))
    
            for p in pre:
                for s in suf:
                    self.table[p+'#'+ s]= idx
                
        

    def f(self, prefix: str, suffix: str) -> int:
        if prefix+ '#'+ suffix in self.table:
            return self.table[prefix+ '#'+ suffix]
        return -1
        
