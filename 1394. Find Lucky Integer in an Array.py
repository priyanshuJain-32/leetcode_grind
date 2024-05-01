class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for n in arr:
            d[n]+=1
        largest = 0
        for k,v in d.items():
            if k==v:
                if k>largest:
                    largest = k
        return largest if largest else -1