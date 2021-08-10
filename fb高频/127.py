class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        bq, eq, nq = set([beginWord]), set([endWord]), set()
        step = 1
        while bq:
            wordSet -= bq
            for word in bq:
                for nxtWord in [word[:i] + ch + word[i+1:] for i in range(len(word)) for ch in string.ascii_lowercase]:

                    if nxtWord in eq:
                        return step + 1
                    if nxtWord in wordSet:
                        nq.add(nxtWord)
            step += 1
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0
                
        
        
        
