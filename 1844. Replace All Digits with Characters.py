class Solution:
    def replaceDigits(self, s: str) -> str:
        a = ""
        if len(s)==1:
            return s
        for i in range(0,len(s)-1,2):
            a += s[i] + chr(ord(s[i])+int(s[i+1]))
        return a+s[i+2:]