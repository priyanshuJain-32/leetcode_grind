class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pointsA = {
            "r0" :0,
            "r1" :0,
            "r2" :0,
            "c0" :0,
            "c1" :0,
            "c2" :0,
            "d1" :0,
            "d2" :0
        }
        pointsB = {
            "r0" :0,
            "r1" :0,
            "r2" :0,
            "c0" :0,
            "c1" :0,
            "c2" :0,
            "d1" :0,
            "d2" :0
        }
        n = len(moves)
        for i in range(0,n,2):
            pointsA["r"+str(moves[i][0])]+=1
            pointsA["c"+str(moves[i][1])]+=1
            if moves[i][0]==moves[i][1]:
                pointsA["d1"]+=1
            if moves[i][0]+moves[i][1]==2:
                pointsA["d2"]+=1

        for i in range(1,n,2):
            pointsB["r"+str(moves[i][0])]+=1
            pointsB["c"+str(moves[i][1])]+=1
            if moves[i][0]==moves[i][1]:
                pointsB["d1"]+=1
            if moves[i][0]+moves[i][1]==2:
                pointsB["d2"]+=1
        if 3 in pointsA.values():
            return "A"
        if 3 in pointsB.values():
            return "B"
        if n<9:
            return "Pending"
        return "Draw"