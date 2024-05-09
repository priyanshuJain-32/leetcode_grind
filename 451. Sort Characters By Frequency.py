class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        newD = defaultdict(list)
        for k,v in d.items():
            newD[v].append(k)
        d = ''
        for k in sorted(newD,reverse=True):
            for v in newD[k]:
                d += k*v
        return d