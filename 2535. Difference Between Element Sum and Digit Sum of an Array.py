class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digitSum(n):
            n = str(n)
            ans = 0
            for i in n:
                ans += int(i)
            return ans
        a = 0
        b = 0
        for i in nums:
            a+=i
            b+= digitSum(i)
        return abs(a-b)