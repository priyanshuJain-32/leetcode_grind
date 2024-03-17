class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        ret = [""]*len(s)
        for i in s:
            ret[int(i[-1])-1] = i[:-1]
        return " ".join(ret)