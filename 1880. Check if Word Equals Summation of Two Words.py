class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(Word):
            nW = ""
            for c in Word:
                nW += str(ord(c)-97)
            return int(nW)
        
        fW = convert(firstWord)
        sW = convert(secondWord)
        tW = convert(targetWord)
        return fW+sW==tW