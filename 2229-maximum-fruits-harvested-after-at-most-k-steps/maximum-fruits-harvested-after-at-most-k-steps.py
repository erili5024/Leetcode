class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pos = [p for p, _ in fruits]
        amounts = [a for _, a in fruits]
        psa = [0]
        for i in amounts:
            psa.append(psa[-1] + i)
        maxed = 0 
        n = len(fruits)
        left = 0 
        for right in range(n):
            while left <= right:
                leftdistance = pos[left]
                rightdistance = pos[right]
                steps = min(abs(startPos - leftdistance) + rightdistance - leftdistance,
                            abs(startPos - rightdistance) + rightdistance - leftdistance)
                if steps <= k:
                    break
                left += 1
            if left <= right:
                maxed = max(maxed, psa[right + 1] - psa[left])
        return maxed
