class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # s1, s2 = s[:len(s)//2], s[len(s)//2:]
        d = 1
        i = 0
        n = len(s)
        vowels = 0
        while i<n:
            if i==n//2:
                d = -1
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                vowels += d
            i+=1
        return vowels==0