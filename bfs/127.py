class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bq, eq = {beginWord}, {endWord}
        n = len(endWord)
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        wordSet.remove(endWord)
        steps = 0
        while bq:
            steps += 1
            nq = set()
            for word in bq:
                for nxtWord in [word[:i]+char+word[i+1:] for i in range(n) for char in string.ascii_lowercase]:
                    if nxtWord in eq:
                        return steps + 1
                    if nxtWord in wordSet:
                        nq.add(nxtWord)
                        wordSet.remove(nxtWord)

            bq = nq
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0





# Method 1: birdirectional bfs


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList= set(wordList)
        l= len(beginWord)
        if endWord not in wordList:
            return 0
        s1, s2= {beginWord}, {endWord}
        wordList.remove(endWord)
        step= 0
        
        while s1 and s2:
            step+= 1
            if len(s1)> len(s2):
                s1, s2= s2, s1
            s= set()
            for word in s1:
                nwords= [(word[:i]+ t+ word[i+1:]) for t in string.ascii_lowercase for i in range(l)]
                for nw in nwords:
                    if nw in s2: 
                        return step+ 1
                    if nw not in wordList:
                        continue
                    wordList.remove(nw)
                    s.add(nw)
            s1= s
        return 0
    
    
    
# Method 1: single directional bfs, normal

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList= set(wordList)
        if endWord not in wordList:
            return 0
        res= []
        q= deque([(beginWord, 1)])
        while q:   
            cur, steps= q.popleft()
            if cur== endWord:
                return steps
            
            for i in range(len(cur)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    nword= cur[:i]+ char+ cur[i+1:]
                    if nword not in wordList:
                        continue
                    wordList.remove(nword)
                    q.append((nword, steps+ 1))
        return 0
                    
