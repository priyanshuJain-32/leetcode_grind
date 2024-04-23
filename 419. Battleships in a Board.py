class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=="X":
                    board[i][j]="."
                    self.dfs(board,i,j,m,n)
                    count+=1
        return count
    def dfs(self,board,i,j,m,n):
        queue = [(i,j)]
        while queue:
            I,J = queue.pop()
            for r,c in (I+1,J),(I-1,J),(I,J-1),(I,J+1):
                if 0<=r<m and 0<=c<n and board[r][c]=="X":
                    board[r][c]="."
                    queue.append((r,c))