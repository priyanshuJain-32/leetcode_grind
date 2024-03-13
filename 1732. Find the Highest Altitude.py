class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0]*(n+1)
        maxi = 0
        for i in range(n):
            prefix[i+1] = prefix[i]+gain[i]
            if maxi<prefix[i+1]:
                maxi = prefix[i+1]
        return maxi