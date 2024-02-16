class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ret = []
        for i in candies:
            if i+extraCandies>=m:
                ret.append(True)
                continue
            ret.append(False)
        return ret