class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        counter = 0
        for i in s:
            if i == t[counter]:
                counter += 1
            if counter >= len(t):
                return 0
        return (len(t) - counter)