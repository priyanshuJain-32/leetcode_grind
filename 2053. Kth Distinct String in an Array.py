class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        dist = []
        n = 0
        for i,v in d.items():
            if v==1:
                dist.append(i)
                n+=1
        if n<k:
            return ""
        return dist[k-1]