class Solution:
    def __init__(self):
        self.saved = {0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.saved:
            return self.saved[n]
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        self.saved[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.saved[n]