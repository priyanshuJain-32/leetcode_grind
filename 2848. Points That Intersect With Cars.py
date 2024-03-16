class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for a,b in nums:
            ans = ans.union(set(range(a,b+1)))
        return len(ans)