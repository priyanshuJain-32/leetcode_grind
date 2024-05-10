class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL = 0
        count = 0
        for i in nums:
            if i:
                count += 1
            else:
                maxL = max(count,maxL)
                count = 0
        maxL = max(maxL,count)
        return maxL