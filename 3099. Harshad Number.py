class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        t = x
        while t:
            s+= t%10
            t//=10
        return s if x%s==0 else -1