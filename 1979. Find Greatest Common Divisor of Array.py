class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = max(nums)
        sn = min(nums)

        while mn%sn!=0:
            mn, sn = sn, mn%sn
        return sn