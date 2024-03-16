class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        suffix = list(accumulate(reversed(nums)))
        suffix.reverse()
        for i in range(len(prefix)):
            if prefix[i]==suffix[i]:
                return i
        return -1