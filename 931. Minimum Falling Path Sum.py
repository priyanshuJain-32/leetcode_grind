class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i!=0:
                    if j==0:
                        matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                    elif j==n-1:
                        matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1])
                    else:
                        matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])
        return min(matrix[-1])