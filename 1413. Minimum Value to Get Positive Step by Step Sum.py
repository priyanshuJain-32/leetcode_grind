class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1 - min(list(accumulate(nums))),1)