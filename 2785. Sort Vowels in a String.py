class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"A","a","e","E","i","I","o","O","u","U"}
        asc = []
        pos = []
        string = list(s)
        for i in range(len(string)):
            if string[i] in vowels:
                asc.append(string[i])
                pos.append(i)
        asc.sort()
        k = 0
        for i in pos:
            string[i] = asc[k]
            k+=1
        return "".join(string)