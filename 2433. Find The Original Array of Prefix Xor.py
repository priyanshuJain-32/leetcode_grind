class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret = [pref[0]]
        for i in range(len(pref)-1):
            ret.append(pref[i]^pref[i+1])
        return ret
