class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while a%b!=0:
                a,b = b,a%b
            return b
        
        n = len(str1)
        m = len(str2)

        a = n if n>m else m
        b = m if n>m else n

        l = gcd(a,b)

        multiplier1 = a//l
        multiplier2 = b//l

        short = str2 if n>m else str1
        longer = str1 if n>m else str2
        
        for i in range(l,0,-1):
            if short[:i]*multiplier1 == longer and short[:i]*multiplier2==short:
                return short[:i]
        return ""