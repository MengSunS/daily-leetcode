class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        q, nq = set([beginWord]), set()
        graph = collections.defaultdict(list)
        found = False
        while q:
            wordSet -= q
            for word in q:
                for nxtWord in [word[:i] + ch + word[i+1:] for i in range(len(word)) for ch in string.ascii_lowercase]:
                    if nxtWord in wordSet:
                        nq.add(nxtWord)
                        graph[word].append(nxtWord)
                        if nxtWord == endWord:
                            break
            q, nq = nq, set()
        
       
        
        def dfs(word, path):
            nonlocal found
            if found: return 
            if word == endWord:
                self.res = path[:]
                found = True
                return 
            for nxt in graph[word]:
                dfs(nxt, path + [nxt])
                
        found = False  
        self.res = None
        dfs(beginWord, [beginWord])   
        return self.res
                        
                        
            
        
