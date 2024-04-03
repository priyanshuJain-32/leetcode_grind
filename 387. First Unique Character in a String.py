class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Third way
        # d = collections.defaultdict(int)
        # e = collections.defaultdict(int)
        # n = len(s)
        # for k,c in enumerate(s):
        #     d[c] = k
        # for k,c in enumerate(s[::-1]):
        #     e[c] = k
        # for c in s:
        #     if d[c]==n-e[c]-1:
        #         return d[c]
        # return -1

        # Second way
        for i in range(len(s)):
            if s.find(s[i])==s.rfind(s[i]):
                return i
        return -1

        # First way
        # seen = set()
        # dup = set()
        # for c in s:
        #     if c in seen:
        #         dup.add(c)
        #     seen.add(c)
        # single = seen-dup
        # for i in range(len(s)):
        #     if s[i] in single:
        #         return i
        # return -1