class TrieNode:
    def __init__(self):
        self.children= {}
        self.words= set()

class Trie:
    def __init__(self):
        self.root= TrieNode()
        
    def start_with(self, word):
            
        node= self.root
        for ch in word:
            if ch not in node.children:
                return []
            node= node.children[ch]   
        return node.words
    
   
    def insert(self, word):
        node= self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]= TrieNode()
            node= node.children[ch]
            node.words.add(word)
            
       
        

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie= Trie()
        self.cache= ''
        self.node= self.trie.root
        self.counts= defaultdict(int)
        for i in range(len(sentences)):
            self.trie.insert(sentences[i])
            self.counts[sentences[i]]= times[i]
        
        

    def input(self, c: str) -> List[str]:
        if c!= '#':  
            self.cache+= c
            words= self.trie.start_with(self.cache)
            res= []
            for word in words:
                res.append((self.counts[word], word))
            return [sentence for freq, sentence in sorted(res, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.trie.insert(self.cache)
            self.counts[self.cache]+= 1
            self.cache= ''
        
        
        
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
