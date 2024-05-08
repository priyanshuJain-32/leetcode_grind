class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        L = []
        for i,s in enumerate(score):
            L.append([s,i])
        L.sort(key = lambda x: x[0],reverse=True)
        
        rank = ["Gold Medal","Silver Medal","Bronze Medal"]
        j = 0
        for i in range(len(L)):
            L[i][0] = rank[j]
            j+=1
            if j==3:
                break
        for i in range(3,len(L)):
            L[i][0] = str(i+1)
        
        L.sort(key = lambda x: x[1])
        for i in range(len(L)):
            yield L[i][0]