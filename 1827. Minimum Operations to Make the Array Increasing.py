class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                diff = nums[i]-nums[i+1]
                ans += diff + 1
                nums[i+1] += diff + 1
        return ans