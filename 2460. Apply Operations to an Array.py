class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        m = 0
        n = len(nums)
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        ans = []
        for i in nums:
            if i>0:
                ans.append(i)
        del nums
        return ans+[0]*(n-len(ans))