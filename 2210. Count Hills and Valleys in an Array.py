class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = j = 1
        count = 0
        while i<len(nums)-1:
            if nums[j-1]<nums[i]>nums[i+1] or nums[j-1]>nums[i]<nums[i+1]:
                count += 1
                i += 1
                j = i
                continue
            i += 1
        return count