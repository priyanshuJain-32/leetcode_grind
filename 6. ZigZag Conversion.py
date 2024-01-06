class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Third draft
        d = 1
        L = [""]*numRows
        j = 0
        if numRows==1:
            return s
        for i in s:
            L[j] += i
            j+=d
            if j==numRows-1 or j==0:
                d*=-1
        return "".join(L)

        
        # First draft
#        n = len(s)
#        d = 1
#        L = [""]*numRows
#        i = 0
#        j = 0
#        if numRows==1:
#            return s
#        while i<n:
#            while d==1 and i<n:
#                L[j] += s[i]
#                j+=1
#                i+=1
#                if j==numRows-1:
#                    d=-1
#
#            while d==-1 and i<n:
#                L[j] += s[i]
#                j-=1
#                i+=1
#                if j==0:
#                    d=1
#        return "".join(L)
#
#        # Second draft
#        n = len(s)
#        d = 1
#        L = [""]*numRows
#        i = 0
#        j = 0
#        if numRows==1:
#            return s
#        while i<n:
#            L[j] += s[i]
#            j+=d
#            i+=1
#            if j==numRows-1 or j==0:
#                d*=-1
#        return "".join(L)
