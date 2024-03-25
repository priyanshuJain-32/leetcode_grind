class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for i,s in enumerate(strs):
            try:
                strs[i] = int(s)
                if strs[i]>max_val:
                    max_val = strs[i]
            except:
                strs[i] = len(s)
                if strs[i]>max_val:
                    max_val = strs[i]
        return max_val