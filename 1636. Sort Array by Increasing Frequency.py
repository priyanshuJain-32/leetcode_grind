class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] +=1
        l = defaultdict(list)
        for k,v in d.items():
            l[v].append(k)
        del d
        ans = []
        for v in l.values():
            v.sort(reverse=True)
        for k in sorted(l):
            for i in l[k]:
                ans.extend([i]*k)
            # ans.extend([[i]*k for i in l[k]])
        return ansgi