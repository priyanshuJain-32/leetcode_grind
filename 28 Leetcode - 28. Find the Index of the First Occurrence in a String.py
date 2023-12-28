class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i, j = m-1, m-1
        match = 0
        while j<n:
            if haystack[j]==needle[i]:
                j -= 1
                i -= 1
                match += 1
                if i==-1:
                    return j+1
                continue
            else:
                j += 1 + match
                match = 0
                i = m-1
        return -1
