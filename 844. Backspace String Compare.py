class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(t):
            b = []
            for j in t:
                if j=="#":
                    if b:
                        b.pop()
                else:
                    b.append(j)
            return b
        def check(a,b):
            if len(a)!=len(b):
                return False
            for l,k in zip(a,b):
                if l!=k:
                    return False
            return True
        return check(convert(s),convert(t))
