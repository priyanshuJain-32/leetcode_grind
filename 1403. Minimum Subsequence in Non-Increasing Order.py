class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        bsum = sum(nums)
        fsum = 0
        for i in range(len(nums)):
            fsum+=nums[i]
            bsum-=nums[i]
            if fsum>bsum:
                return nums[:i+1]
        return nums