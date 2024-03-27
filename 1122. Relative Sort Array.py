class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {k:[] for k in arr2}
        d[-1] = []
        for i in arr1:
            if i not in d:
                d[-1].append(i)
            else: d[i].append(i)
        arr1 = []
        arr2.append(-1)
        d[-1].sort()
        for i in arr2:
            arr1.extend(d[i])
        return arr1