class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==1:
            return matrix[0]
        rowS, rowE, colS, colE = 0, len(matrix), 0, len(matrix[0])
        end = rowE*colE
        start = 0
        ret = []
        
        while start < end:
            
            # moving right
            if start<end:
                for i in range(colS, colE):
                    ret.append(matrix[rowS][i])
                    start +=1
                rowS += 1

            # moving down
            if start<end:
                for i in range(rowS, rowE):
                    ret.append(matrix[i][colE-1])
                    start +=1
                colE -=1
            
            # moving left
            if start<end:
                for i in range(colE-1, colS-1, -1):
                    ret.append(matrix[rowE-1][i])
                    start +=1
                rowE -=1
            
            # moving up
            if start<end:
                for i in range(rowE-1, rowS-1, -1):
                    ret.append(matrix[i][colS])
                    start +=1
                colS +=1

        return ret
