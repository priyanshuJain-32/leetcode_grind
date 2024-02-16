class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ret = 0
        for i in accounts:
            ret = max(ret, sum(i))
        return ret