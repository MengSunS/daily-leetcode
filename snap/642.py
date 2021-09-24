class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.words = set()
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.words.add(word)
            
    def start_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.words
        

            
class AutocompleteSystem:
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.freq = collections.defaultdict(int)
        for i in range(len(sentences)):
            self.trie.insert(sentences[i])
            self.freq[sentences[i]] = times[i]
        self.path = ''
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.path)
            self.freq[self.path] += 1
            self.path = ''
            return []
        self.path += c
        words = self.trie.start_with(self.path)
        res = []
       
        return sorted(list(words), key=lambda x: (-self.freq[x], x))[:3]
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
