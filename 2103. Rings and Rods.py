class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        for i in range(1,len(rings),2):
            d[rings[i]].add(rings[i-1])
        cnt = 0
        for k,v in d.items():
            if len(v)==3:
                cnt +=1
        return cnt