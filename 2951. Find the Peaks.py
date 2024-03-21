class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        i = 1
        while i<len(mountain)-1:
            if mountain[i-1]<mountain[i]>mountain[i+1]:
                ans.append(i)
                i+=2
            else:
                i+=1
        return ans