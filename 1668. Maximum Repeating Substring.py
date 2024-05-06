class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i = len(sequence)//len(word)
        temp = word*i
        while temp not in sequence:
            i-=1
            temp = word*i
        return i