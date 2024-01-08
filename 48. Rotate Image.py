import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # First approach
        n = len(matrix)
        for i in range(n-1):
            for j in range(i, n-1-i):
                matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i], matrix[i][j]  = matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]
        
        # Second approach
        # Transpose matrix
        # for i in range(n):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # # Reverse each row
        # for i in range(n):
        #     matrix[i].reverse()
