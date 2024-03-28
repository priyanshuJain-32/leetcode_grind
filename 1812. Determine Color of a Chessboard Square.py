class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return (ord(c[0])-97+int(c[1]))%2==0