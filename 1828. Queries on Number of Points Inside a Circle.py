class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret = []
        for q in queries:
            count = 0
            q[2]**=2
            for p in points:
                if ((q[1]-p[1])**2 + (q[0]-p[0])**2)<=q[2]:
                    count+=1
            ret.append(count)
        return ret
