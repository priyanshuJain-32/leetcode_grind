class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        for i in range(n-1):
            left[i+1] = left[i]+nums[i]
            right[n-i-2] = right[n-i-1]+nums[n-i-1]
        return [abs(i-j) for i,j in zip(left, right)]