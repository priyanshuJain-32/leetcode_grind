class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        exchange = 0
        while numBottles>0:
            total += numBottles
            exchange += numBottles
            numBottles = exchange // numExchange
            exchange = exchange%numExchange
        return total