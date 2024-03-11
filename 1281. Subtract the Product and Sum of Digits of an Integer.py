class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        m = 1
        a = 0
        for i in n:
            temp = int(i)
            m*=temp
            a+=temp
        return m-a