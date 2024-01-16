class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        count = 0
        for laser in bank:
            prev = max(m, prev)
            count = laser.count("1")

            if count:
                ans += count * prev
                prev = 0
        return ans
