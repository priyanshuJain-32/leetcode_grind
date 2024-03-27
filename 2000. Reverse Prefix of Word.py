class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            p = word.index(ch)
            return word[p::-1]+word[p+1:]
        except:
            return word