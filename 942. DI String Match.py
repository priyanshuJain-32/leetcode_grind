class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        a = list(range(0,n+1))
        i = 0
        j = n
        k = 0
        ans = []
        while i<j and k<n:
            if s[k]=="I":
                ans.append(a[i])
                i+=1
            elif s[k]=="D":
                ans.append(a[j])
                j-=1
            k+=1
        ans.append(a[i])
        return ans