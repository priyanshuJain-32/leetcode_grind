class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in target:
            d[i]+=1
        for j in arr:
            d[j]-=1
            if d[j]<0:
                return False
        return True