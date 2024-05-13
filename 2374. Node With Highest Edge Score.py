class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0]*len(edges)
        for idx,p in enumerate(edges):
            scores[p] += idx
        maxS,maxIdx = 0,0
        for idx,s in enumerate(scores):
            if s>maxS:
                maxS = s
                maxIdx = idx
        return maxIdx