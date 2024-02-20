class Solution:
    def arraySign(self, nums: List[int]) -> int:
        minusC = 0
        for i in nums:
            if i<0:
                minusC += 1
            elif i==0:
                return 0
        return -1 if minusC%2 else 1