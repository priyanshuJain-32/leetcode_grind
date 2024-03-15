class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        d = defaultdict(int)
        for a,b in indices:
            for i in range(a,m*n,m):
                d[i]+=1
            for j in range(b*m,b*m+m):
                d[j]+=1
        ans = 0
        for k,v in d.items():
            if v%2!=0:
                ans += 1
        return ans