class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Traverse through a matrix
        # Find the O on the edge and mark them and neighbors as "V"
        # Then move to the next "O" and switch them to "X" if they are not "V"
        # if they are "V" mark them as "O"
        
        m,n = len(board), len(board[0])

        for j in range(n):
            if board[0][j]=="O": 
                board[0][j]="V"
                self.helper(board,0,j,m,n)
            if board[m-1][j]=="O":
                board[m-1][j]="V"
                self.helper(board,m-1,j,m,n)

        for i in range(m):
            if board[i][0]=="O":
                board[i][0]="V"
                self.helper(board,i,0,m,n)
            if board[i][n-1]=="O":
                board[i][n-1]="V"
                self.helper(board,i,n-1,m,n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="V":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"

    def helper(self,board,i,j,m,n):
        que = [(i,j)]
        while que:
            r,c = que.pop()
            for i,j in [(r,c+1),(r+1,c),(r-1,c),(r,c-1)]:
                if 0<=i<m and 0<=j<n and board[i][j]=="O":
                    board[i][j]="V"
                    que.append((i,j))