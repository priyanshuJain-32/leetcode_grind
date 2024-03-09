class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n-1):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                if a+b<target:
                    count += 1
        return count