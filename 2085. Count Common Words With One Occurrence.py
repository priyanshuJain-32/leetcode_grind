class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d = defaultdict(int)
        for w in words1:
            d[w]+=1
        for k,v in d.items():
            if v>1:
                d[k] = -1
        for w in words2:
            d[w]-=1
        return list(d.values()).count(0)