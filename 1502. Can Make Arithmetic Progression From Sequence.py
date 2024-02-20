class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        for a,b in zip(arr[:-1], arr[1:]):
            if b-a!=diff:
                return False
        return True