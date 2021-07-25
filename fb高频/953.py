class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {c: i for i, c in enumerate(order)}
        m = [[idx[c] for c in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(m, m[1:]))



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for a, b in zip(w1, w2):
                if idx[a] < idx[b]:
                    break
                elif idx[a] > idx[b]:
                    return False
        return True
        
