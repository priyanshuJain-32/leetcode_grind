class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for a in nums:
            if 10<=a<=99 or 1000<=a<=9999 or a==100000:
                ans += 1
        return ans