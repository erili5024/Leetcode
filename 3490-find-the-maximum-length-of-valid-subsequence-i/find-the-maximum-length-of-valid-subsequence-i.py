class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        options = [[0] * 2 for _ in range(2)]
        maximum = 0 
        for i in nums:
            remainder = i%2
            p = 0
            while p < 2:
                options[p][remainder] = options[remainder][p] + 1
                maximum = max(options[p][remainder], maximum)
                p += 1
        return maximum
