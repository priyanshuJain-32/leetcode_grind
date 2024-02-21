class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = nums.copy()
        if nums[-1]>nums[0]:
            temp.sort()
        else:
            temp.sort(reverse=True)
        return temp==nums