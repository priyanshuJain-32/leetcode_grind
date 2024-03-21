class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i in rectangles:
            d[min(i)]+=1
        return d[max(d.keys())]