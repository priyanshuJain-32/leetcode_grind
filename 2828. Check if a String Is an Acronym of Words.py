class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        a = ""
        for w in words:
            a+=w[0]
        return a==s