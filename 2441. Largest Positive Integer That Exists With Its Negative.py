class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        max_int = -1
        for n in nums:
            if -1*n in seen:
                max_int = max(abs(n), max_int)
            seen.add(n)
        return max_int