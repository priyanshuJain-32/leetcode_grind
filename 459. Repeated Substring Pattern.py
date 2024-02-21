class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Brilliant solution in community 27 ms
        ss = (s+s)[1:-1]
        return s in ss
        
        # My solution 104 ms
        n = len(s)
        if n==1:
            return False
        for i in range(1,n//2+1):
            if s[:i]*(n//i)==s:
                return True
        return False