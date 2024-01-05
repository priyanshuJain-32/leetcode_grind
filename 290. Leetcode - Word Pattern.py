class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charWordMap = {}
        s = s.split()
        if len(pattern)!=len(s):
            return False
        for p,w in zip(pattern,s):
            if (p not in charWordMap):
                if (w not in charWordMap.values()):
                    charWordMap[p] = w
                else:
                    return False
            elif (charWordMap[p]!=w):
                return False
        return True
