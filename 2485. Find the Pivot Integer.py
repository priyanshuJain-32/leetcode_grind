class Solution:
    def pivotInteger(self, n: int) -> int:
        # First Approach
        x = math.sqrt(n*(n+1)/2)
        a = int(x)
        if x==a:
            return a
        return -1
        
        # Second Approach
        # l = list(range(1,n+1))
        # i = n-2
        # lsum = sum(l)
        # rsum = l[-1]

        # while not (lsum<=rsum) and i>-1:
        #     lsum -= l[i+1]
        #     rsum += l[i]
        #     print(lsum, rsum)
        #     i-=1
        # return i+2 if lsum==rsum else -1