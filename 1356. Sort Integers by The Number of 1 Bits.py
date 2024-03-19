class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = []
        for i in arr:
            l.append((bin(i)[2:].count("1"),i))
        l.sort()
        return [v for k,v in l]