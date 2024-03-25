class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        min_row = set()
        for i in range(m):
            min_row.add(min(matrix[i]))
        ans = []
        for j in range(n):
            max_col = 0
            for i in range(m):
                if matrix[i][j]>max_col:
                    max_col = matrix[i][j]
            if max_col in min_row:
                ans.append(max_col)
        return ans