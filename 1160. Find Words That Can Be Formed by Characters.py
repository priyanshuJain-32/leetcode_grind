class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def checkgood(d, char):
            for c in char:
                d[c]-=1
                if d[c]<0:
                    return 0
            return len(char)
        d = defaultdict(int)
        for c in chars:
            d[c]+=1
        ans = 0
        for word in words:
            temp_d = d.copy()
            ans += checkgood(temp_d,word)
        del temp_d
        return ans