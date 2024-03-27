class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l, r, p, c = 0, 0, 1, 0
        n = len(nums)

        while r<n:
            p *= nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            c += r-l+1
            r+=1
        return c