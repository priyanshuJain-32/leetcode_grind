class Solution:
    def finalString(self, s: str) -> str:
        ret = ""
        for ch in s:
            if ch=="i":
                ret = ret[::-1]
            else:
                ret += ch
        return ret