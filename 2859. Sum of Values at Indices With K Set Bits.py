class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def convert(n):
            if n==0:
                return 0
            return convert(n//2)+n%2
        ans = 0
        for i in range(len(nums)):
            if convert(i)==k:
                ans += nums[i]
        return ans