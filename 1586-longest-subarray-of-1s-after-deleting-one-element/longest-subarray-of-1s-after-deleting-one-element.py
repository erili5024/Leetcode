class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        zerocounter = 0 
        maxlen = 0 
        zeros = []
        p1 = 0 
        p2 = 0
        i = 0
        while p1 < len(nums):
            if nums[p1] == 0:
                zerocounter += 1
                zeros.append(p1)
            if zerocounter > k:
                p2 = zeros[i]
                p2 += 1
                i += 1
                zerocounter = zerocounter - 1
            maxlen = max(maxlen, p1-p2)
            p1 += 1
        return maxlen
            

        