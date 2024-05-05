class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Community solution inspired
        m, n = len(dungeon), len(dungeon[0])
        health = [[0 for _ in range(n)] for _ in range(m)]
        health[-1][-1] = max(1,1-dungeon[-1][-1])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j!=n-1:
                    health[i][j] = max(1,health[i][j+1]-dungeon[i][j])
                elif i!=m-1 and j==n-1:
                    health[i][j] = max(1,health[i+1][j]-dungeon[i][j])
                elif i!=m-1 and j!=n-1:
                    health[i][j] = max(1,min(health[i+1][j],health[i][j+1])-dungeon[i][j])

        return health[0][0]

        # 1000 dumb ways of not thinking
        # healthDip = [[[0,0] for _ in range(n)] for _ in range(m)]
        
        # healthDip[0][0][0] = dungeon[0][0]
        # healthDip[0][0][1] = min(dungeon[0][0],0)
        
        # for i in range(m):
        #     for j in range(n):
                
        #         if i==0 and j!=0:
        #             healthDip[i][j][0] = dungeon[i][j]+healthDip[i][j-1][0]
        #             healthDip[i][j][1] = min(healthDip[i][j][0],healthDip[i][j-1][1])
                
        #         elif j==0 and i!=0:
        #             healthDip[i][j][0] = dungeon[i][j]+healthDip[i-1][j][0]
        #             healthDip[i][j][1] = min(healthDip[i][j][0],healthDip[i-1][j][1])
        #             # dungeon[i][j] += dungeon[i-1][j]
                
        #         elif i!=0 and j!=0:
        #             if healthDip[i][j-1][1]>healthDip[i-1][j][1]:
        #                 healthDip[i][j][0] = dungeon[i][j]+healthDip[i][j-1][0]
        #                 healthDip[i][j][1] = min(healthDip[i][j][0],healthDip[i][j-1][1])
        #             elif healthDip[i][j-1][1]<healthDip[i-1][j][1]:
        #                 healthDip[i][j][0] = dungeon[i][j]+healthDip[i-1][j][0]
        #                 healthDip[i][j][1] = min(healthDip[i][j][0],healthDip[i-1][j][1])
        #             else:
        #                 # print('here',i,j)
        #                 healthDip[i][j][0] = max(healthDip[i][j-1][0],healthDip[i-1][j][0])+dungeon[i][j]
        #                 healthDip[i][j][1] = min(healthDip[i][j][0],healthDip[i][j-1][1])
        #                 # dungeon[i][j] += max(dungeon[i-1][j],dungeon[i][j-1])
        # print(healthDip)
        # return -healthDip[-1][-1][-1]+1