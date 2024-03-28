class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = str(num)
        m = len(n)
        if m==1:
            return True
        if n[-1]=="0":
            return False
        return True