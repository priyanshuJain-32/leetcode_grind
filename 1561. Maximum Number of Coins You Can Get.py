class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        n = len(piles)
        b_limit = n//3
        for i in range(n-1,b_limit-1,-2):
            ans += piles[i-1]
        return ans