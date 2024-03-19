class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums[0:2])
        second = min(nums[0:2])
        i = 2
        while i<len(nums):
            if second<nums[i]<first:
                second = nums[i]
            elif nums[i]>=first:
                second = first
                first = nums[i]
            i+=1
        return (first-1)*(second-1)g