class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        counter = 0 
        start = set()
        for i in startWords:
            start.add(frozenset(i))
        for q in targetWords:
            target = frozenset(q)
            for char in target:
                reduced = target - frozenset([char])
                if reduced in start:
                    counter += 1
                    break

        return counter
                
        