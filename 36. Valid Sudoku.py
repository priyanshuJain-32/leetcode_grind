class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(L):
            dCount = {}
            for d in L:
                if d not in dCount:
                    dCount[d]=0
                dCount[d]+=1
            for k,v in dCount.items():
                if v>1:
                    if k==".":
                        continue
                    else:
                        return False
            return True

        def checkCol(M):
            for i in range(9):
                L = []
                for j in range(9):
                    L.append(M[j][i])
                if not checkRow(L):
                    return False
            return True
        
        def checkBox(M):
            L1, L2, L3 = [], [], []
            for i in range(9):
                for j in range(3):
                    L1.append(M[i][j])
                for j in range(3,6):
                    L2.append(M[i][j])
                for j in range(6,9):
                    L3.append(M[i][j])
                if i==2 or i==5 or i==8:
                    if not (checkRow(L1) and checkRow(L2) and checkRow(L3)):
                        return False
                    L1, L2, L3 = [], [], []
            return True

        for i in board:
            if not checkRow(i):
                return False

        if not checkCol(board):
            return False

        if not checkBox(board):
            return False
        return True
