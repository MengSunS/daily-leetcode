class TrieNode:
    def __init__(self):
        self.children= {}
        self.is_word= False
    
    
    
    
    
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= TrieNode()
      
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node= self.root
        for c in word:
            if c in node.children:
                node= node.children[c]
            else:
                node.children[c]= TrieNode()
                node= node.children[c]
        node.is_word= True
        
            
       

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        
        node= self.root
        return self.dfs(word, node)
    
    def dfs(self, word, node):
        if word=='':
            return node and node.is_word
        
        c= word[0]
        if c!='.':
            if c in node.children:
                return self.dfs(word[1:], node.children[c])
            else:
                return False
        
        else:
            for child in node.children:
                if self.dfs(word[1:], node.children[child]):
                    return True
            return False
            
        
