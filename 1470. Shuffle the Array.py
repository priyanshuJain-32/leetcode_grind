class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        ret = []
        for i,j in zip(range(n//2), range(n//2, n)):
            ret.extend([nums[i]] + [nums[j]])
        return ret
