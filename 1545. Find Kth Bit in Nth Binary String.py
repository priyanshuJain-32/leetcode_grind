class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        self.d = defaultdict(str)
        def make(n):
            if n in self.d:
                return self.d[n]
            if n==1:
                return '0'
            self.d[n] = make(n-1)+'1'+invert(make(n-1))[::-1]
            return self.d[n]
        def invert(s):
            ans = ''
            for i in s:
                if i=="0":
                    ans += '1'
                else:
                    ans += '0'
            return ans
        return make(n)[k-1]