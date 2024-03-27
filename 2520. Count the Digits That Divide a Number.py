class Solution:
    def countDigits(self, num: int) -> int:
        d = collections.defaultdict(int)
        for n in str(num):
            d[n]+=1
        ans = 0
        for k,v in d.items():
            if k!="1":
                if num%int(k)==0:
                    ans += v
            else:
                ans += v
        return ans