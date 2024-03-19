class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        return len(set(d.values()))==1