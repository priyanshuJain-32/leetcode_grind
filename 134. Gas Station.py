class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = start = deficit = 0 # start with calculating tank and total deficit
        for i in range(len(gas)):
            tank += gas[i] - cost[i] # keep filling and emptying tank
            if tank < 0: # if tank is negative just increment the start
                deficit, tank, start = deficit + tank, 0, i+1 # keep a total of fuel vs cost in deficit, reset tank and new start
        return start if deficit+tank>-1 else -1