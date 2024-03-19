class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums.remove(max(nums))
        try:
            nums.remove(min(nums))
            return nums.pop() if nums else -1
        except: return -1