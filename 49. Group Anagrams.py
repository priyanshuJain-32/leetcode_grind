class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for i in strs:
            key = "".join(sorted(i))
            try:
                D[key].append(i)
            except:
                D[key] = [i]
        return D.values()
