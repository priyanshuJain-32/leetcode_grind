class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        m = len(nums)//2
        if m==0:
            return nums[m]
        if m==1:
            return nums[-1] if nums[0]==nums[1] else nums[0]
        if m%2==0:
            if nums[m]==nums[m+1]:
                return self.singleNonDuplicate(nums[m+2:])
            elif nums[m]==nums[m-1]:
                return self.singleNonDuplicate(nums[:m-1])
        else:
            if nums[m]==nums[m+1]:
                return self.singleNonDuplicate(nums[:m])
            elif nums[m]==nums[m-1]:
                return self.singleNonDuplicate(nums[m+1:])
        return nums[m]