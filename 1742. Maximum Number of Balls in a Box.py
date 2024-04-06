class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def calc(n):
            ans = 0
            while n:
                ans += n%10
                n //= 10
            return ans
        d = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            d[calc(i)]+=1
        return max(d.values())