class Solution:
    def jump(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i]+i, nums[i-1])
        steps = 0
        i = 0
        while i < len(nums)-1:
            steps+=1
            i = nums[i]
        return steps
