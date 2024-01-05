class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0, 0
        counts = []
        n = len(s)
        if n<2:
            return n
        while j<n:
            if s[j] in s[i:j]:
                counts.append(j-i)
                i = i+1+s[i:j].index(s[j])
                j+=1
            else:
                j+=1
            if j==n:
                counts.append(j-i)
        return max(counts) if len(counts)>0 else j-i
