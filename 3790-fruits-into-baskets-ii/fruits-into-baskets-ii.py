class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        j = 0
        counter = 0 
        for i in fruits:
            while j < len(baskets):
                if i <= baskets[j]:
                    baskets[j] = -1
                    break
                j += 1
            j = 0 
        for i in baskets:
            if i != -1:
                counter += 1
        return counter 