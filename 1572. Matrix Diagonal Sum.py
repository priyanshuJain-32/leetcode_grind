class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)
        total = 0
        for i in range(dim):
            if (i,i)==(i,dim-i-1):
                total += mat[i][i]
                continue
            total += mat[i][i] + mat[i][dim-i-1]
        return total