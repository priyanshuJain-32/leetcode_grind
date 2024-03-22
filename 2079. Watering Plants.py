class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = 0
        steps = 0
        can = capacity
        while i<len(plants):
            if plants[i]<=can:
                can -= plants[i]
                plants[i]=0
                steps += 1
                i+=1
            else:
                steps += 2*(i)
                can = capacity
        return steps