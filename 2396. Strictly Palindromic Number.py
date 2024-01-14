class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isPalindrome(s: str) -> bool:
            return s==s[::-1]
        for i in range(2,n-1):
            s = ''
            m = n
            while m>0:
                s+=str(m%i)
                m//=i
            if not isPalindrome(str(s)):
                return False
        return True
