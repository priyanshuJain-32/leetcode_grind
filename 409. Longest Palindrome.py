class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for c in s:
            d[c]+=1
        ans = 0
        flag = False
        for k in set(s):
            if d[k]>0:
                if d[k]%2==0:
                    ans += d[k]
                else:
                    ans += d[k]-1
                    flag = True
        return ans +1 if flag else ans