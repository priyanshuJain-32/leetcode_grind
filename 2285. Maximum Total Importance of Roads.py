class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0]*n
        for u,v in roads:
            count[u]+=1
            count[v]+=1
        count.sort()
        ans = 0
        for c,i in zip(count,range(1,n+1)):
            ans += c*i
        return ans