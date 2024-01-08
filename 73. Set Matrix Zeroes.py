class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = set()
        n = len(matrix)
        m = len(matrix[0])
        flag = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    flag = True
                    col.add(j)
                    continue
            if flag:
                flag = False
                matrix[i] = [0]*m
                
        for j in col:
            for i in range(n):
                matrix[i][j] = 0
