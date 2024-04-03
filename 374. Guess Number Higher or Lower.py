class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        while l<=n:
            m = (l+n)//2
            res = guess(m)
            if res==1:
                l = m+1
            elif res==-1:
                n=m-1
            else:
                return m