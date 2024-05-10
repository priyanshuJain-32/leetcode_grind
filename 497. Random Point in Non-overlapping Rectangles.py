class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.points = []
        self.totalPoints = 0
        for a,b,x,y in rects:
            nPoints = (x-a+1)*(y-b+1)
            self.totalPoints += nPoints
            self.points.append(self.totalPoints)
        self.l = len(rects)

    def pick(self) -> List[int]:
        pickRect = random.randint(1,self.totalPoints)
        for idx, nPoint in enumerate(self.points):
            if pickRect<=nPoint:
                break

        a,b,x,y = self.rects[idx]
        X,Y = random.randint(a,x),random.randint(b,y)
        
        return [X,Y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()