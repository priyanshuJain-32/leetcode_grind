class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        i,j = 0,0
        while i<target:
            if j<nums[i]:
                j = nums[i]
            i+=1
            if j==0:
                return False
            j-=1
        return True
