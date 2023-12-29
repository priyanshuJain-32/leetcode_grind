class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for i in magazine:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        try:
            for j in ransomNote:
                chars[j] -= 1
            print(chars)
            for v in chars.values():
                if v<0:
                    return False
            return True 
        except:
            return False
