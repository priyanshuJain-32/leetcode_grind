class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        for j in range(n):
            flag = False
            maxi = -1
            for i in range(m):
                if matrix[i][j]==-1:
                    flag = True
                maxi = max(maxi, matrix[i][j])
            if flag:
                for i in range(m):
                    if matrix[i][j]==-1:
                        matrix[i][j] = maxi
        return matrix