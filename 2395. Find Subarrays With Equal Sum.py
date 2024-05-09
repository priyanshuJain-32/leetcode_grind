class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dp = set()
        for i in range(len(nums)-1):
            a = nums[i]+nums[i+1]
            if a in dp:
                return True
            dp.add(a)
        return False