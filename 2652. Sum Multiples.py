class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = set()
        for i in [3,5,7]:
            a=i
            while a<n+1:
                ans.add(a)
                a+=i
        return sum(ans)