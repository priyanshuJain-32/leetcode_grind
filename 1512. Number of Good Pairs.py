class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        def fact(n):
            if n<=1:
                return 1
            return n*fact(n-1)
        
        def combinationCalc(n):
            return fact(n)/(fact(n-2)*2)
        counter = defaultdict(int)
        
        for i in nums:
            counter[i] += 1

        ret = 0
        for v in counter.values():
            if v==1:
                continue
            ret += combinationCalc(v)
        return int(ret)