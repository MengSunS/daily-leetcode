class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.word = word
        
    def find_prefix(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
                if node.word:
                    return node.word
            else:
                return word
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        res = []
        for word in sentence.split():
            res.append(trie.find_prefix(word))
        return ' '.join(res)
            
       




class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        def find_prefix(word):
            n = len(word)
            for i in range(n):
                if word[:i + 1] in dictionary:
                    return word[:i + 1]
            return word
        
        res = []
        for word in sentence.split():
            res.append(find_prefix(word))
        return ' '.join(res)
             
