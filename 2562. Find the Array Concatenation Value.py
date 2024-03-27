class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        total = 0
        while i<j:
            total += int(str(nums[i])+str(nums[j]))
            i, j = i+1, j-1
            
        if i==j:
            total += nums[i]
        return total