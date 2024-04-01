class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(rows):
            dr = abs(i-rCenter)
            for j in range(cols):
                dc = abs(j-cCenter)
                d[dr+dc].append([i,j])
        ans = []
        for k in sorted(d):
            ans.extend(d[k])
        return ans