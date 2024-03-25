class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r = []
        for n in nums:
            if nums[abs(n)-1]<0:
                r.append(abs(n))
            nums[abs(n)-1]*=-1
        return r