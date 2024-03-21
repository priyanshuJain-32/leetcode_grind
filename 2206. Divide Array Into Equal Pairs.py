class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        for v in d.values():
            if v&1:
                return False
        return True