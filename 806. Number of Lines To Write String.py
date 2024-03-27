class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        n = len(s)
        i, rt = 0, 1
        row_max = 100
        while i<n:
            if row_max<widths[ord(s[i])-97]:
                row_max = 100
                rt += 1
            row_max>=widths[ord(s[i])-97]
            row_max -= widths[ord(s[i])-97]
            i+=1
        return [rt, 100-row_max]