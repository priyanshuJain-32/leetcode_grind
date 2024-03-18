class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s
        c = ""
        for i in range(n//2):
            if s[i]==s[n-i-1]:
                c+=s[i]
            else:
                c+=chr(min(ord(s[i]),ord(s[n-i-1])))
        return c + s[i+1] + c[::-1] if n%2 else c+c[::-1]