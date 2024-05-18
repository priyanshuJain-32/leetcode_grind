class Solution:
    def minOperations(self, s: str) -> int:
        def calc(s,start):
            count = 0
            for c in s:
                if c!=start[-1]:
                    count += 1
                start += "1" if start[-1]=="0" else "0"
            return count
        return min(calc(s,"0"),calc(s,"1"))