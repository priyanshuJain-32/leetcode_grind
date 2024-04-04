class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n,m = 0,0
        for c in s:
            if c==letter:
                m+=1
            n+=1
        return int(m/n*100)