class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
        # d = defaultdict(int)
        # for i in s:
        #     d[i]+=1
        # return len(d.keys())