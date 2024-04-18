class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        self.prefix = [self.makePref(word) for word in words[1:]]
        self.suffix = [self.makePref(word[::-1]) for word in words[1:]]
        i, m = 0, len(words)
        ans = 0
        while i<m-1:
            for p,s in zip(self.prefix[i:],self.suffix[i:]):
                if self.match(words[i],p) and self.match(words[i][::-1],s):
                    ans += 1
            i+=1
        return ans
    def match(self,word,p):
        curr = p
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return True
    def makePref(self,word):
        pref = {}
        curr = pref
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['*'] = ''
        return pref