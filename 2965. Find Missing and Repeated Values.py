class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_sum = n**2*(n**2+1)/2
        seen = set()
        actual_sum = 0
        ans = [0,0]
        for i in grid:
            for j in i:
                if j in seen:
                    ans[0] = j
                actual_sum+=j
                seen.add(j)
        ans[1] = int(expected_sum - actual_sum+ans[0])
        return ans