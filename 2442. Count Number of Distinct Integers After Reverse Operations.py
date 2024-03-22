class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = set(nums)
        revs = set()
        for i in nums:
            revs.add(int(str(i)[::-1]))
        return len(nums.union(revs))