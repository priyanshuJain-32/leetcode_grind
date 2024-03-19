class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxi = 0
        for c,u in boxTypes:
            if c<=truckSize and truckSize>0:
                truckSize -= c
                maxi += c*u
            elif c>truckSize and truckSize>0:
                maxi += truckSize*u
                return maxi
        return maxi