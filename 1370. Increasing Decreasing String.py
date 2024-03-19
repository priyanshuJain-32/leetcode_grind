class Solution:
    def sortString(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] +=1
        l = []
        total = len(s)
        seen = 0
        while seen<total:
            temp = ""
            for i in sorted(d.keys()):
                if d[i]>0:
                    d[i]-=1
                    temp += i
                    seen += 1
            l.append(temp)
        ans = ""
        for i in range(len(l)):
            if i%2:
                ans += l[i][::-1]
            else:
                ans += l[i]
        return ans