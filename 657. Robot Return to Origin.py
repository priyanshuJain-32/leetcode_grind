class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moveMap = {"L":0, "R":0, "D":0, "U":0}
        for i in moves:
            moveMap[i] += 1
        return moveMap["L"]==moveMap["R"] and moveMap["U"]==moveMap["D"]

        # moveMap = {"L":[-1,0], "R":[1,0], "D":[0,-1], "U":[0,1]}
        # pos = 
        # for i in moves:
        #     pos[0] += moveMap[i][0]
        #     pos[1] += moveMap[i][1]
        # return [0,0]==pos