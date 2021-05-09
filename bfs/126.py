# Method 1: bidirectional bfs + dfs

# bidirectional bfs 

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        bq, eq = set([beginWord]), set([endWord])
        wordSet = set(wordList)
        if endWord not in wordSet: return []
        graph = defaultdict(list)
        found = False
        rev = False
        n = len(endWord)
        while bq and not found:
            wordSet -= bq
            nq = set()
            for word in bq:
                for newWord in [word[:i]+char+word[i+1:] for i in range(n) for char in string.ascii_lowercase]:
                    if newWord in wordSet:
                        if newWord in eq:
                            found = True
                        nq.add(newWord)
                        if not rev:
                            graph[word].append(newWord)    
                        else:
                            graph[newWord].append(word) 
            bq = nq
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev
        
        def btr(x):
            return [[x]] if x == endWord else [[x] + path for child in graph[x] for path in btr(child)]
        
        
        if not found: return []
        return btr(beginWord)
       
                
                            
        
 # Method 2: single directional bfs + dfs

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        q = set([beginWord])
        wordSet = set(wordList)
        graph = defaultdict(list)
        found = False
        while q and not found:
            wordSet -= q
            nq = set()
            for word in q:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in wordSet:
                            if newWord == endWord:
                                found = True
                            nq.add(newWord)
                            graph[word].append(newWord)               
            q = nq
        
        def btr(x):
            return [[x]] if x == endWord else [[x] + path for child in graph[x] for path in btr(child)]
        
        
        if not found: return []
        return btr(beginWord)








# Method 3: BFS. not preferred, 费空间
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet= set(wordList)
        if endWord not in wordSet: return []
        layer= defaultdict(list)
        layer[beginWord]= [[beginWord]]
        
        while layer:
            nextLayer= defaultdict(list)
            for word in layer:
                if word== endWord:
                    return layer[word]
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord= word[:i]+ char+ word[i+1:]
                        if newWord in wordSet:  #这里不需要全局visited去重，同一层的不同单词可以在下一层到达同一个单词
                            nextLayer[newWord]+= [path+ [newWord] for path in layer[word]]
            wordSet-= set(nextLayer.keys())
            layer= nextLayer
        return []
