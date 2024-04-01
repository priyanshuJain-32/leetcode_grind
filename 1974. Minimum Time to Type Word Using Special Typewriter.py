class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        prev = ord("a")
        for w in word:
            w = ord(w)
            d = abs(w-prev)
            ans += min(d,26-d)
            prev = w
        return ans