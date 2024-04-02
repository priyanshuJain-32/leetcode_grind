class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i,m,n = 0,0,len(s)
        while n>m and i<len(words):
            m += len(words[i])
            i+=1
        return s=="".join(words[:i])