class Solution:
    def totalMoney(self, n: int) -> int:
        d = n//7
        r = n%7
        total = 0
        for i in range(d):
            total += 28 + 7*i
        for j in range(1,r+1):
            total += j+d
        return total