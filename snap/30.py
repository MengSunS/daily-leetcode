class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        substring_size = word_size * len(words)
        res = []
        for left in range(len(s) - substring_size + 1):
            need = Counter(words)
            missing = len(words)
            for i in range(left, left + substring_size, word_size):
                word = s[i: i + word_size]
                if need.get(word, 0) > 0:
                    need[word] -= 1
                    missing -= 1
                else:
                    break
                if missing == 0:
                    res.append(left)
        return res
                        
            
        
