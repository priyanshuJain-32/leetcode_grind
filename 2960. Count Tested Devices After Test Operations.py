class Solution:
    def countTestedDevices(self, bP: List[int]) -> int:
        cnt = 0
        for b in bP:
            if b>cnt:
                cnt += 1
        return cnt