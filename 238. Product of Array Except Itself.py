class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        for i in range(1,n):
            pre[i] = nums[i-1]*pre[i-1]
        for i in range(n-2,-1,-1):
            suf[i] = nums[i+1]*suf[i+1]
        return [i*j for i,j in zip(pre, suf)]
