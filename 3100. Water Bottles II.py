class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empBottles = numBottles
        def refill(empBottles, numExchange):
            refills = 0
            while empBottles>=numExchange:
                empBottles -= numExchange
                numExchange+=1
                refills+=1
            return refills, empBottles, numExchange
        while True:
            numBottles, empBottles, numExchange = refill(empBottles, numExchange)
            if numBottles == 0:
                break
            drunk += numBottles
            empBottles += numBottles
        return drunk