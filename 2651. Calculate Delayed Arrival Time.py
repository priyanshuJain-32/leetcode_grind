class Solution:
    def findDelayedArrivalTime(self, aT: int, dT: int) -> int:
        ans = aT+dT
        if ans>=24:
            return ans%24
        return ans