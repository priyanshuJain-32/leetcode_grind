class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i,j,maxi = 0,1,0
        while j<len(colors):
            if colors[i]!=colors[j]:
                maxi = j-i
            j+=1
        j-=1
        while i<len(colors):
            if colors[i]!=colors[j]:
                maxi = max(maxi, j-i)
            i+=1
        return maxi