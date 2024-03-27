class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]
        cnt = 0
        for i,j in zip_longest(a[::-1],b[::-1], fillvalue="0"):
            if i!=j:
                cnt += 1
        return cnt