class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        options = [[0] * k for _ in range(k)]
        maxed = 0 
        q = 0 
        for i in nums:
            remainder = i % k
            q= 0
            while q < k:
                options[q][remainder] = options[remainder][q] + 1
                maxed = max(options[q][remainder], maxed)
                q += 1
        return maxed