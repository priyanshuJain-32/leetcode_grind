class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Can use binary search to make the solution faster than O(n2)

        # My simple approach
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j]>-1:
                    break
                cnt += 1
        return cnt