class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        shortlist = []
        for idx,(a,b) in enumerate(points):
            if a==x or b==y:
                d = abs(a-x) + abs(b-y)
                shortlist.append((d,idx))
        shortlist.sort(key= lambda x: x[0])
        return shortlist[0][1] if shortlist else -1