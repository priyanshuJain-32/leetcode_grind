class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sum(nums)
        s_ = sum(set(nums))
        n = len(nums)
        n_ = len(set(nums))
        return int((s-s_)/(n-n_))