class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [i for i in range(1,6)]
        for i in range(1,n):
            for j in range(1,5):
                dp[j] += dp[j-1]
        return dp[4]