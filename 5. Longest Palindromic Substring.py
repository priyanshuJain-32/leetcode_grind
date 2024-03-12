class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        n = len(s)
        if n<=1:
            return s

        def give_pal(left, right, n):
            while left>-1 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
            return (s[left+1:right],right-left-1)
        
        max_pal = s[0]
        max_len = 1
        for i in range(n-1):
            po, lo = give_pal(i,i,n)
            pe, le = give_pal(i,i+1,n)
            if lo>max_len:
                max_len = lo
                max_pal = po
            if le>max_len:
                max_len = le
                max_pal = pe
        return max_pal