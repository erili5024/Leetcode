class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq = Counter(word1)
        values = list(freq.values())
        freq1 = Counter(word2)
        values1 = list(freq1.values())
        if Counter(values) == Counter(values1) and set(word1) == set(word2):
            return True
        return False