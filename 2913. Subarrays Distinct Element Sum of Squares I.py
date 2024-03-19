class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(n):
            ns = set()
            for j in range(i,n):
                ns.add(nums[j])
                s+= len(ns)**2
        return s