class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0

        up = True if startPos[0]>homePos[0] else False

        y_start = startPos[0]+1 if not up else startPos[0]-1
        y_end = homePos[0]+1 if not up else homePos[0]-1
        dire_y = 1 if not up else -1

        left = True if startPos[1]>homePos[1] else False
        
        x_start = startPos[1]+1 if not left else startPos[1]-1
        x_end = homePos[1]+1 if not left else homePos[1]-1
        dire_x = 1 if not left else -1
        
        for i in range(y_start,y_end,dire_y):
            ans += rowCosts[i]
        
        for j in range(x_start,x_end,dire_x):
            ans += colCosts[j]
            
        return ans