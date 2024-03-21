class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums)*k+int((k-1)*(k)/2)