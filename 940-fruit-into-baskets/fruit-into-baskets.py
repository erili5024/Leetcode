class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        p1 = -1
        p2 = -1
        i = 0
        counter = 0
        maxed = 0
        while i < len(fruits):
            if p1 == -1:
                p1 = i
                counter += 1
            elif p2 == -1 and fruits[p1] != fruits[i]:
                p2 = i 
                counter += 1
            elif p2 == -1 and fruits[p1] == fruits[i]: 
                counter += 1
            elif fruits[i] != fruits[p1] and fruits[i] != fruits[p2]:
                counter = i - p2 + 1
                p1 = p2 
                p2 = i
            elif fruits[i] == fruits[p1]:
                p1 = p2
                p2 = i
                counter += 1
            elif fruits[i] == fruits[p2]:
                counter += 1
            maxed = max(maxed, counter)
            i += 1
        return maxed




