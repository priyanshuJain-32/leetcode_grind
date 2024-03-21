class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champ = 0
        max_s = 0
        for i in range(len(grid)):
            score = grid[i].count(1)
            if score>max_s:
                max_s = score
                champ = i
        return champ