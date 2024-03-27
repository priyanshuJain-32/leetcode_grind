class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        m, l = max(nums), min(nums)
        return max(0, m-l - 2*k)