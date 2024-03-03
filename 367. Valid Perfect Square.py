class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = num**(0.5)
        return a==int(a)