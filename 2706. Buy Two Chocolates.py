class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        fmin = smin = 101
        for p in prices:
            if p<fmin:
                smin = fmin
                fmin = p
            elif p<smin:
                smin = p
        left = money -fmin-smin
        if left>=0:
            return left
        return money