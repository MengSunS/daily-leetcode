class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def goat(w, i):
            if w[0].lower() not in vowels:
                w = w[1:] + w[0]
            w += 'ma' + 'a' * (i + 1)
            return w
        return ' '.join(goat(w, i) for i, w in enumerate(sentence.split(' ')))
