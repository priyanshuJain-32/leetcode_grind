class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            slope1 = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        except:
            slope1 = "Not defined"
        for i in range(len(coordinates)-1):
            try:
                slope2 = (coordinates[i][1]-coordinates[i+1][1])/(coordinates[i][0]-coordinates[i+1][0])
            except:
                slope2 = "Not defined"
            if slope1!=slope2:
                return False
        return True