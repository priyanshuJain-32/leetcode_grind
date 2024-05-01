class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        dim = 8
        flag = False
        for i in range(dim):
            for j in range(dim):
                if board[i][j]=='R':
                    x,y = i,j
                    flag = True
                    break
            if flag:
                break
        count = 0
        i,j = x,y
        while i>0:
            if board[i-1][j]=='.':
                i-=1
            elif board[i-1][j]=='p':
                count += 1
                break
            else:
                break
        i,j = x,y
        while j>0:
            if board[i][j-1]=='.':
                j-=1
            elif board[i][j-1]=='p':
                count += 1
                break
            else:
                break
        i,j = x, y
        while i<7:
            if board[i+1][j]=='.':
                i+=1
            elif board[i+1][j]=='p':
                count += 1
                break
            else:
                break
        i,j = x, y
        while j<7:
            if board[i][j+1]=='.':
                j+=1
            elif board[i][j+1]=='p':
                count += 1
                break
            else:
                break
        return count